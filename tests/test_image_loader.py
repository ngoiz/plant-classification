import unittest
import os
import plant_classification.imageloader as imageloader
import pandas as pd

class TestImageLoader(unittest.TestCase):

    images_directory = imageloader.images_directory

    def test_image_format(self):

        img_loader = imageloader.ImageLoader(self.images_directory)

        img_loader.extension = 'png'

        with self.subTest(msg='Image Name'):
            img_name = img_loader.image_name(1)
            self.assertEqual(img_name.lower(), '0001.png')
        
        with self.subTest(msg='Image Filename'):
            img_filename = img_loader.image_filename(30)
            self.assertEqual(img_filename, os.path.join(self.images_directory, '0030.png'))

        # try changing the directory
        with self.subTest(msg='Changing to inexistent directory'):
            img_loader.directory = 'a/fake/path'
            self.assertEqual(img_loader.directory, self.images_directory)

    def test_image_operations(self):

        img_loader = imageloader.ImageLoader(self.images_directory)

        img = img_loader.open_image(1)

        with self.subTest(msg='Check format'):
            self.assertEqual(img.format.lower(), img_loader.extension.lower())

    def test_dataframes(self):
        img_loader = imageloader.ImageLoader(self.images_directory)

        img_loader.create_dataframes()

        desired_column_names = {'file', 'label', 'name'}
        for column_name in img_loader.df.columns:
            with self.subTest(msg=f'Check column {column_name} is correct'):
                if column_name not in desired_column_names:
                    raise pd.errors.MergeError(f'Columns {column_name} not in {desired_column_names}')
