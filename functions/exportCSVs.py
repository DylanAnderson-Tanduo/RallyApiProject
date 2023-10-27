import csv


def export_to_csv(rally, entity_type, filename, known_fields, project=None, iteration=None, mode='w'):
    query_criteria = None
    if iteration and ('HierarchicalRequirement' in entity_type or 'Task' in entity_type):
        query_criteria = f'Iteration.Name = "{iteration}"'

    with open(filename, mode, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[])
        all_fieldnames = set(known_fields)

        entities = rally.get(entity_type, fetch=True, project=project,
                             query=query_criteria, pagesize=10, limit=10)
        entity_dicts = []

        for entity in entities:
            entity_dict = {'Artifact Type': entity_type}
            entity_dict.update({k: v for k, v in known_fields.items()})

            for attribute in entity.attributes():
                value = getattr(entity, attribute)
                if value is not None:
                    if hasattr(value, 'Name'):
                        entity_dict[attribute] = value.Name
                    else:
                        entity_dict[attribute] = value

                all_fieldnames.add(attribute)

            entity_dicts.append(entity_dict)

        writer.fieldnames = list(all_fieldnames)
        if mode == 'w':
            writer.writeheader()

        for entity_dict in entity_dicts:
            writer.writerow(entity_dict)
