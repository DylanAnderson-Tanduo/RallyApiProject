from pyral import Rally


def connect_to_rally(apikey, workspace, server):
    try:
        rally = Rally(server=server, apikey=apikey, workspace=workspace)
        print("Successfully connected to Rally.")
        return rally
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
