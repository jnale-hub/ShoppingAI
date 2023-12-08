import unittest
import tempfile
import csv
from shopping.py import load_data 

class TestLoadData(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.temp_file_name = self.temp_file.name

        # Write sample data to the temporary file
        csv_writer = csv.writer(self.temp_file)
        csv_writer.writerow(['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration',
                             'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues',
                             'SpecialDay', 'Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType',
                             'VisitorType', 'Weekend', 'Revenue'])
        csv_writer.writerow(['1', '10.5', '2', '20.5', '3', '30.5', '0.2', '0.3', '40.5', '0.1', 'Jan', '1', '1', '1', '1', 'Returning_Visitor', 'TRUE', 'True'])
        csv_writer.writerow(['2', '15.3', '3', '25.2', '4', '35.2', '0.3', '0.4', '45.8', '0.2', 'Feb', '2', '2', '2', '2', 'New_Visitor', 'FALSE', 'False'])
        csv_writer.writerow(['3', '20.1', '4', '30.7', '5', '40.7', '0.4', '0.5', '50.3', '0.3', 'Mar', '3', '3', '3', '3', 'Returning_Visitor', 'TRUE', 'True'])
        csv_writer.writerow(['4', '25.8', '5', '35.9', '6', '45.9', '0.5', '0.6', '55.6', '0.4', 'Apr', '4', '4', '4', '4', 'New_Visitor', 'FALSE', 'False'])

        self.temp_file.seek(0)

    def tearDown(self):
        # Close and remove the temporary CSV file
        self.temp_file.close()

    def test_load_data(self):
        # Call the load_data function with the temporary file
        evidence, labels = load_data(self.temp_file_name)

        self.assertEqual(len(evidence), 17)
        self.assertEqual(len(labels), 1)
        self.assertEqual(evidence[0][0], 1)  # Adjust these assertions based on your sample data
        self.assertEqual(labels[0], 1)  # Adjust these assertions based on your sample data

if __name__ == '__main__':
    unittest.main()
