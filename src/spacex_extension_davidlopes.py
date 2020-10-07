from ruxit.api.base_plugin import RemoteBasePlugin
import requests


class SpaceXExtension(RemoteBasePlugin):

    def query(self, **kwargs):

        # Get the list of ships from the spacex api
        ships = self.get_ships()

        # Get the unique names of the groups
        ship_types = set([ship["ship_type"] for ship in ships])

        # Save the groups to a dictionary to be used later
        groups = {}
        for ship_type in ship_types:
            groups[ship_type] = self.topology_builder.create_group(f"{ship_type} David Lopes", f"{ship_type} David Lopes")

        for ship in ships:
            # Grab the Group object for this ship
            ship_group = groups[ship["ship_type"]]

            # Create the custom device
            custom_device = ship_group.create_device(f"{ship['ship_id']} David Lopes", f"{ship['ship_name']} David Lopes")

            # Send a simple metric
            custom_device.absolute("fuel", ship["fuel"])


    def get_ships(self):
        url = "http://ec2-3-235-75-78.compute-1.amazonaws.com/v3/ships"
        self.logger.info(f"Calling {url}...")
        return requests.get(url).json()




