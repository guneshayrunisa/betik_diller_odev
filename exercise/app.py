from src.dosya_islemleri import read_csv, write_json, write_text
from src.processing import stats, build_report, clean_data
from src.dekorator import required_column

def main():
    read_doc = r"C:\Users\gunes\OneDrive\Masaüstü\betik_diller_odev-main\calculator\people.csv"
    write_json_doc = r"C:\Users\gunes\OneDrive\Masaüstü\betik_diller_odev-main\exercise\data\people_clean.json"
    write_stats_doc = r"C:\Users\gunes\OneDrive\Masaüstü\betik_diller_odev-main\exercise\data\stats.json"
    write_txt = r"C:\Users\gunes\OneDrive\Masaüstü\betik_diller_odev-main\exercise\data\stats_txt.txt"

    rows = read_csv(read_doc)

    required_check = required_column({"name", "age", "city"})(lambda r: r)
    rows = required_check(rows)

    cleaned_rows = clean_data(rows)

    st = stats(cleaned_rows)

    write_json(write_json_doc, cleaned_rows)
    write_json(write_stats_doc, st)
    write_text(write_txt, build_report(st))

    print("İşlem tamamlandı ✅")

if __name__ == "__main__":
    main()
