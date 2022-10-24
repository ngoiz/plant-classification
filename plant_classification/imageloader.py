"""
Loads images from database and returns array of tensors
"""
from distutils import extension
import pandas as pd
import os
import plant_classification.utils as plant_utils
from PIL import Image

images_directory = os.path.join(plant_utils.PACKAGE_DIRECTORY, 'flower_images')


class ImageLoader:

    def __init__(self, directory:str):
        self._directory = None

        self.directory = directory
        self.extension = 'png'
        self.image_name_format = '{image_id:04g}.{fmt_extension:s}'

        self.labels = None # pd.Dataframe() containing the label:label_name

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, path_to_dir:str):
        path_to_dir = os.path.abspath(path_to_dir)
        if not os.path.isdir(path_to_dir):
            print(f'Specified directory not found {path_to_dir}' \
                    f'\nReverting to default directory {images_directory}')
            path_to_dir = images_directory
            if not os.path.isdir(path_to_dir):
                print('Default directory not found')
                raise FileNotFoundError
        self._directory = path_to_dir

    def image_name(self, image_id:int) -> str:
        return self.image_name_format.format(image_id=image_id, 
                                             fmt_extension=self.extension)

    def image_filename(self, image_id:int) -> str:
        return os.path.join(self.directory, self.image_name(image_id))

    def open_image(self, image_id:int) -> Image:
        return Image.open(self.image_filename(image_id))

    def create_dataframes(self):
        flower_labels_df = pd.read_csv(self.directory + '/flower_labels.csv',
                                       dtype={'file': str,
                                              'label': int})
        labels_df = pd.read_csv(self.directory + '/labels.csv', 
                                index_col='label',
                                dtype={'label': int,
                                        'name': str})

        self.labels = labels_df # add runtime test for unique data

        assert self.labels.index.nunique() == self.labels['name'].count(), 'Repeated label in labels dataframe.'

        self.df = flower_labels_df

        # Prepend abspath to file column
        self.df['file'] = self.df['file'].apply(lambda x: add_parent_folder(x, self.directory))
        
        self.df = self.df.merge(self.labels, left_on='label', right_index=True)

def add_parent_folder(path, parent_folder):
    return os.path.join(parent_folder, path)