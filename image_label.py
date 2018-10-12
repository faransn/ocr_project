import os
import config


def get_image_labels(path):
    labels = []
    for folder, subs, files in os.walk(unicode(path, 'utf-8')):
        for file in files:
            if file.endswith(config.image_format):
                labels.append(file.replace(config.image_format, ""))
    return labels
