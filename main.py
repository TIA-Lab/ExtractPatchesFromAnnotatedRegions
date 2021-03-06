import argparse
import py_wsi

def ExtractPatches(args):
    file_dir = args.wsi_folder
    output_location = args.output_folder
    xml_dir = file_dir
    patch_size = args.patch_size
    magnification = args.magnification
    db_name = "patch_db"
    overlap = 0
    labels_str = args.labels
    label_map={}
    labels_ids = labels_str.split(",")
    for label_id in labels_ids:
        splt = label_id.split(":")
        label_map[splt[0]] = splt[1]
    label_map["Normal"] = 0
    turtle = py_wsi.Turtle(file_dir, output_location, db_name, xml_dir=xml_dir, label_map=label_map, storage_type='disk')
    turtle.sample_and_store_patches(patch_size, magnification, overlap, load_xml=True, limit_bounds=True)

def main():
    # Training settings
    parser = argparse.ArgumentParser(description='Extraction of the annotated regions from WSIs')
    parser.add_argument('--wsi-folder', default="F:/Projects/HEROHE/Dataset/DataSets/",
                        help='Folder where all WSI images are kept')
    parser.add_argument('--output-folder', default="F:/Projects/HEROHE/Dataset/Annotations/",
                        help='Folder where you want to store annotated images')
    parser.add_argument('--patch-size', type=int, default=256, metavar='N',
                        help='Patch Size')
    parser.add_argument('--magnification', type=int, default=10, metavar='N',
                        help='Select the suitable magnification to set resolution, default is 10X')
    parser.add_argument('--labels', default="dcis:1,invasive:2,lcis:3,invaisve:4",
                        help='Give comma separated labels for annotations you want to be extracted, give each label as labelname:labelid')
    args = parser.parse_args()
    ExtractPatches(args)

if __name__ == "__main__":
    # execute only if run as a script
    main()