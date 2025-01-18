from pathlib import Path
import os

def main():
    keyword_path = input("키워드 셋 경로를 입력해주세요")
    print(keyword_path)

    if not os.path.isfile(keyword_path):
        print("키워드 셋 경로를 다시 입력해주세요.")
        return

    with open(keyword_path, "r", encoding="UTF=8") as k:
        keywords = k.read().split(", ")


    evidence_path = input("증거자료를 입력해주세요").replace("\\", "/")
    
    if not os.path.isdir(evidence_path):
        print("증거자료 경로를 다시 한번 확인해주세요.")
        return

    for p in Path().glob(evidence_path + "/**/*"):
        if os.path.isfile(p):
            print(p)
            with open(p, "r", encoding="UTF=8") as k:
                data = k.read()
                for keyword in keywords:
                    print(keyword, keyword in data)
