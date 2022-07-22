from flask import render_template, redirect, request
from models import *
from exchange import exchange
from app import *
from forms import *
from werkzeug.utils import secure_filename
from extensions import share
import os


@app.route("/adding")
def add_news():
    

    content1 = '''Fəal təhsil dəstəkçisi olan Yelo Bank bu dəfə gənc hüquqşünaslara qapılarını açdı. Bankın maliyyə və təşkilati dəstəyi ilə ELSA Azerbaijan (Avropa Hüquqşünas Tələbələr Assosiasiyası) tərəfindən İnsan hüquqları I Natiqlik Müsabiqəsi həyata keçirildi. Müsabiqənin 3 gün davam edən yarımfinal və final mərhələləri Bankın Baş ofisinin tədbir zalında baş tutdu. 

30 yaşadək gənc hüquqşünaslar seçdikləri və İnsan hüquqlarını əhatə edən mövzularda 10 dəqiqəlik çıxışlar etdilər. Aralarında Yelo Bank hüquqşünaslarının da yer aldığı münsiflər heyəti iştirakçıları mövzuya hakimlik, natiqlik qabiliyyəti, bədən dili, məzmun, analiz və s. keyfiyyətlərə görə dəyərləndirdilər. Münsif xallarına əsasən yarımfinalda ən yüksək xalı toplamış 7 gənc finala keçmək hüququ qazandı. Final 28 May Müstəqillik günü baş tutdu. Azərbaycan dövlət himninin səsləndirilməsi ilə başlayan final mərhələsinin iştirakçıları bu dəfə eyni mövzuda təsdiq və ya inkar mövqeyində yarışdılar. Çıxışların yekununda münsiflər heyətinin verdikləri xala görə 3 ən yaxşı natiq müəyyənləndirilərək qalib seçildi. Hər 3 qalibə sertifikatlar, pul mükafatı və kubok təqdim olundu.

Yelo Bank Korporativ Sosial Məsuliyyət layihələrini ərsəyə gətirərkən gənclərin fərdi inkişafı və işgüzarlıq qabiliyyətinin artırılmasına xüsusi diqqət edir. Bank il sonunadək cəmiyyətimizə daha çox fayda verəcək digər layihələrin də həyata keçirilməsini planlaşdırır.
 
Bank xidmətləri, o cümlədən, kredit sifarişi haqqında əlavə sualınız var? O zaman 981 nömrəsinə zəng edin və ya Facebook, Instagram  və ya Whatsapp hesablarımıza yazın.

Yelo Bank – Parlaq bankçılıq!'''

    content2 = '''
    İT sahəsində özünü görən və inkişaf etdirmək istəyən gəncləri hədəfləyən Yelo IT Lab proqramına namizədlərin seçimi başa çatıb. Proqram barədə mətbuatda xəbərlər çıxan andan etibarən cəmiyyətdə doğurduğu geniş maraq Yelo Bankın bu sosial təşəbbüsünə yüksək tələbatın olduğunu göstərir. Onlayn ərizələr göndərildikdən sonra namizədlərin seçimi test və fərdi müsahibə olmaqla iki mərhələdə aparıldı. 1400-dən çox iştirakçı arasında ən uyğun 35 nəfər proqramda iştirak haqqı qazandı. Yelo Bank-ın Baş ofisində iştirakçılar təntənəli surətdə qarşılandılar. Açılış tədbirində bank rəhbərliyi və əməkdaşlarının iştirakı ilə təqdimat və ofis turu həyata keçirildi. 3 ay davam edəcək təlim və tədris proqramının yekununda xüsusi fərqlənən məzunlar Yelo Bank-da işlə təmin olunacaq.

Proqramın fəaliyyətinə İT həlləri üzrə ixtisaslaşmış «GNI Software» şirkəti metodoloji dəstək verir. Təlimləri Yelo Bank və «GNI Software» şirkətinin peşəkar əməkdaşları Agile metodikası əsasında aparır. Yelo IT Lab-də öyrədilən təhsil və qazanılan təcrübə tələbələrin fərdi inkişafına, özlərini və layihələrini təqdim etmək bacarıqlarını təkmilləşdirmələyə kömək edəcək. Yelo IT Lab proqramının yaradılmasında əsas məqsəd ölkəmizdə peşəkar İT mütəxəssislərinin hazırlanmasına və bu istiqamətin inkişafına dəstək olmaqdır. 

Bank xidmətləri, o cümlədən, kredit haqqında əlavə sualınız var? O zaman 981 nömrəsinə zəng edin və ya Facebook, Instagram  və ya Whatsapp hesablarımıza yazın.

Yelo Bank – Parlaq bankçılıq!
    '''

    content3 = '''Yelo Bankın Korporativ Sosial Məsuliyyət strategiyasının əsas istiqamətlərindən biri gənclərə dəstək məqsədli layihələrə təşəbbüs göstərməkdir. Bu məqsədlə Yelo Bank ölkəmizdəki aparıcı ali məktəblərlə əməkdaşlığı, karyera tədbirlərində fəal iştirakını artıq bir ənənəyə çevirib. Bankın əməkdaşlarının qatıldığı son tədbirlərdən biri Azərbaycan Dövlət Neft və Sənayə Universiteti və Azərbaycan Dövlət Aqrar Universitetində təşkil edilib. 

Karyera sərgilərində yüzlərlə tələbə və məzunlar Yelo Bankın İnsan Resursları üzrə təmsilçiləri ilə ünsiyyətdə olaraq bankda karyera imkanı, mövcud vakansiyalar haqqında məlumatlar əldə ediblər. Onlara müraciət və işəqəbul prosedurları barədə ətraflı təqdimat edilib. Sərginin iştirakçılarına həmçinin, Bankın istedadlı gənclərə dəstək üçün bir sıra proqramlar həyata keçirdiyi də bildirilib. Yelo Bank müəyyən bilik və bacarıqlara malik, amma iş təcrübəsi olmayan gənclərə imkanlar yaradır. Onlara təcrübə qazanmaqda dəstək verir. 

Xatırladaq ki, hazırda Bankda karyerasını İT sahəsində qurmaq istəyən gənclərə yönəlik “Yelo IT Lab” proqramı başlayıb. Qarşıda Yelo Bank-ın ənənəvi yay təcrübə proqramının başlaması, “Walk and Talk” səyyar mentorluq layihəsinin həyata keçirilməsi də nəzərdə tutulub.

Bank xidmətləri, o cümlədən, daşınmaz əmlak təminatlı kredit haqqında əlavə sualınız var? O zaman 981 nömrəsinə zəng edin və ya Facebook, Instagram  və ya Whatsapp hesablarımıza yazın.

Yelo Bank – Parlaq bankçılıq!'''
    news1 = News(title= "Yelo Bank-da İnsan hüquqları üzrə müsabiqə baş tutdu", content= content1, image_url= "../../../static/images/yelo.jpeg")
    news2 = News(title= "Yelo It Lab proqramının iştirakçıları bəlli oldu", content= content2, image_url= "../../../static/images/yelo.jpeg")
    news3 = News(title= "Yelo Bank universitetlərlə aktiv əməkdaşlıq edir", content= content3, image_url="../../../static/images/yelo.jpeg")

    news1.save()
    news2.save()    
    news3.save()
    
    return redirect("/")

@app.route("/")
def home():
    
    news = News.query.order_by(News.added_at.desc())[:3]
    return render_template("index.html", all_news = news, exchange = exchange, status=True)


@app.route("/az/news/")
def news():
    
    news = News.query.order_by(News.added_at.desc())
    return render_template("news.html", all_news=news)



    

@app.route("/az/news/<slug>/")
def news_details(slug):
    news = News.query.filter_by(slug=slug).first()
    content= news.content.split("\n")
    return render_template("news_details.html",title = news.title, content=content, image=news.image_url, adding= news.added_at)



@app.route("/individuals/cards/")
def cards():
    cards = Card.query.all()
    for card in cards:

        print(card.id)
    return render_template('cards.html', cards=cards,  status = True)


@app.route("/individuals/cards/<string:card_type>/", methods=['GET', 'POST'])
def card_detailed(card_type):
    if card_type == 'yelo-kart-debet':
        check = '1'
    elif card_type == 'yelo-kart-premium':
        check = '2'
    elif card_type == 'yelo-loan-card':
        check = '3'
    print(card_type)
    post_data = request.form
    form = CardRequestForm()
    if request.method == 'POST':
        form = CardRequestForm(data=post_data)
        if form.validate_on_submit():
            file1_data = form.file1.data
            file2_data = form.file2.data
            file1_data.save(os.path.join(os.path.abspath(os.path.dirname(
                __file__)), app.config['UPLOAD_FOLDER'], secure_filename(file1_data.filename)))
            file2_data.save(os.path.join(os.path.abspath(os.path.dirname(
                __file__)), app.config['UPLOAD_FOLDER'], secure_filename(file2_data.filename)))
            card = Cardreq(cardtype=form.cardtype.data, val=form.val.data, first_name=form.first_name.data,
                           last_name=form.last_name.data, prefiks=form.prefiks.data, phone=form.phone.data, code_word=form.code_word.data, branch=form.branch.data, file1=form.file1.data, file2=form.file2.data)
            card.save()
            return redirect("/success/success-loan-request/")
    card = Card.query.filter(Card.id == check).first()
    main_features = Feature.query.filter(Feature.card_id == check, Feature.type == 'main').all()
    additional_features = Feature.query.filter(Feature.card_id == check, Feature.type == 'additional').all()
    return render_template('detailed-card.html', card=card,  main_features = main_features, additional_features = additional_features, form=form, status=True)


@app.route("/individuals/deposits/")
def deposits():
    deposits = Deposit.query.all()
    return render_template('deposits.html', deposits=deposits, status=True)


@app.route("/individuals/online-services/loan_request/", methods=['GET', 'POST'])
def loan_request():
    post_data = request.form
    form = LoanRequestForm()
    if request.method == 'POST':
        form = LoanRequestForm(data=post_data)
        if form.validate_on_submit():
            loan = Loanreq(salary=form.salary.data, loan=form.loan.data, first_name=form.first_name.data,
                           last_name=form.last_name.data, workplace=form.workplace.data, prefiks=form.prefiks.data, phone=form.phone.data)
            loan.save()
            return redirect("/success/success-loan-request/")
    return render_template('online-services.html', form=form)


@app.route("/success/success-loan-request/")
def success():
    return render_template("success-loan-request.html")

