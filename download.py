import argparse
import bs4
import itertools
import os
import progressbar
import requests
import shutil

URL = 'http://ipilab.usc.edu/BAAweb/'

CORRECTIONS = {
    'JPEGimages/ASIF/ASIF05/5260.jpg': 'JPEGimages/ASIF/ASIF05/5262.jpg',
    'JPEGimages/BLKF/BLKF06/7090.jpg': 'JPEGimages/BLKF/BLKF06/7290.jpg',
    # 'JPEGimages/BLKF/BLKF12/7144.jpg': None,
    'JPEGimages/BLKM/BLKM13/7022.jpg': 'JPEGimages/BLKM/BLKM13/7101.jpg',
    'JPEGimages/CAUF/CAUF14/7126.jpg': 'JPEGimages/CAUF/CAUF14/7154.jpg',
    'JPEGimages/CAUM/CAUM12/7185.jpg': 'JPEGimages/CAUM/CAUM12/7186.jpg'
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', default='.')
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    races = ['ASI', 'BLK', 'CAU', 'HIS']
    genders = ['F', 'M']
    ages = ['%02d' % x for x in range(19)]

    print('Downloading meta information...')
    results = []
    for race, gender, age in progressbar.progressbar(list(itertools.product(races, genders, ages))):
        response = requests.post(URL, data={'Race': race, 'Gender': gender, 'Age': age})
        assert response.status_code == 200
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        for record in soup.find_all('tr'):
            cells = record.find_all('td')
            if len(cells) == 12:
                results.append([cells[0].find('img')['src'].strip()] + [x.text.strip() for x in cells[1:]])
            elif len(cells) == 1:
                pass  # Should be the copyright cell
            elif len(cells) == 0:
                pass  # Should be the header
            else:
                print('Table row does not match expected format')

    print('Downloading images...')
    for record in progressbar.progressbar(results):
        dirname = os.path.join(args.output_dir, os.path.dirname(record[0]))
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        response = requests.get(URL + record[0], stream=True)
        if response.status_code == 404 and record[0] in CORRECTIONS:
            print('Original image "%s" not found, trying "%s"' % (record[0], CORRECTIONS[record[0]]))
            record[0] = CORRECTIONS[record[0]]
            response = requests.get(URL + record[0], stream=True)

        if response.status_code != 200:
            print('Failed to download "%s" with status code %d' % (record[0], response.status_code))
        else:
            with open(os.path.join(args.output_dir, record[0]), 'wb') as ofile:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, ofile)

    print('Writing meta information to disk...')
    with open(os.path.join(args.output_dir, 'meta.csv'), 'w') as ofile:
        for record in results:
            ofile.write(','.join(record))
            ofile.write('\n')
