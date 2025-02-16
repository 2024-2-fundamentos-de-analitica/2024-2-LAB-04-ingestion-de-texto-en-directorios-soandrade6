# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import zipfile
import glob
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    # Función para descomprimir un archivo ZIP
    def decompress_zip(zip_path, extract_to):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

    # Función para crear un directorio si no existe
    def make_output_dir(output_path):
        os.makedirs(output_path, exist_ok=True)

    # Función para generar un dataset a partir de archivos organizados en carpetas
    def create_dataset(input_folder, output_file):
        dataset = [
            (open(file, 'r', encoding='utf-8').read().strip(), sentiment)
            for sentiment in ['negative', 'neutral', 'positive']
            for file in glob.glob(os.path.join(input_folder, sentiment, '*'))
        ]
        df = pd.DataFrame(dataset, columns=['phrase', 'target'])
        df.to_csv(output_file, index=False)
        return df

    # Configuración de rutas
    input_zip, extract_to = 'files/input.zip', 'files'
    output_dir = 'files/output'

    decompress_zip(input_zip, extract_to)
    make_output_dir(output_dir)

    train_df = create_dataset(os.path.join(extract_to, 'input/train'), os.path.join(output_dir, 'train_dataset.csv'))
    test_df = create_dataset(os.path.join(extract_to, 'input/test'), os.path.join(output_dir, 'test_dataset.csv'))

    train_df, test_df
