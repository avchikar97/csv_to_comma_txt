import pandas as pd
import sys

def output_csv_txt(filename: str):
    ### Read, pre-process
    df = pd.read_csv(filename, header=None)
    file = open(f"{filename}.output.txt", 'w')
    output = ""

    df.columns = ['temp_header']

    if df.shape[1] > 1:
        print(f"WARNING: There is more than 1 column in {filename}. Only the first column will be outputted in .txt.")
        data_series = df['temp_header']
        frame = {'temp_header': data_series}
        df = pd.DataFrame(frame)

    df.sort_values('temp_header', ascending=True, inplace=True) #sort

    ### Formulate output
    for name in df['temp_header']:
        output += name + ","
    output = output[:-1] # knock off the last comma

    ### Output
    file.write(output) # nice output
    #print(output) # console print visual confirmation


def csv_to_comma_txt():
    file_list = sys.argv
    del file_list[0] # remove csv_to_comma_txt.py from args

    if len(sys.argv) < 1:
        error = (
            f"ERROR: please specify which .csv files to process\n"
            f"Correct usage: python3 {__file__} \"Animals - Sheet1.csv\" \"Anime list - Sheet1.csv\""
        )
        print(error)
        return

    for file_name in sys.argv:
        print(f"Outputting {file_name} as comma-separated string in {file_name}.output.txt")
        output_csv_txt(file_name)

if __name__ == "__main__":
    csv_to_comma_txt()
