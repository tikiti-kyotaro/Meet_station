from flask import Flask, request, render_template, Markup
from src.equal_location import Equal_locate
from src.find_station import Find_NS

app = Flask(__name__)

STATION_CSV = "./data/station20230327free.csv"
LINE_CSV = "./data/line20230327free.csv"
COMPANY_CSV = "./data/company20230105.csv"

def new_line(sentence):
    return Markup(sentence.replace('\n', '<br>'))


@app.route('/', methods=['GET', 'POST'])
def meet_station():
    if request.method == 'POST':
        location_list = request.form['locates'].replace(",", " ").split()
        if len(location_list) == 0:
            error_info = "住所を入力してください。"
            return render_template("index.html", error_info=error_info)
        el = Equal_locate(location_list=location_list)
        lat, lng, logging_list, target_ll_info = el.main()
        if el.not_address:
            log_mess = "\n".join(logging_list)
            log_mess = new_line(log_mess)
            error_info = "地名に該当する住所がないためもう一度入力してください。市区町村名や近くの有名な場所に変更してください。"
            return render_template("index.html", error_info=error_info, logging_list=log_mess)
        else:
            target_locate = [lat, lng]
            log_mess = "\n".join(logging_list)
            log_mess = new_line(log_mess)

            fn = Find_NS(target_locate=target_locate, station_csv=STATION_CSV, line_csv=LINE_CSV, company_csv=COMPANY_CSV)
            name, line_list = fn.main()
            message2 = f'最寄駅名: {name} \n 路線: {",".join(line_list)}'
            message2 = new_line(message2)
            nearest_station_name = name
            line_name = ", ".join(line_list)
            return render_template('index.html', target_ll_info=target_ll_info, nearest_station_name=nearest_station_name, line_name=line_name, logging_list=log_mess)
    
    else:
        return render_template('index.html', message="")

if __name__ == "__main__":
    app.run(port = 8000, debug=True)
