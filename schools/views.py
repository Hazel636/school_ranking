from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import psycopg2

def sec_ON_schools(request):
    conn = psycopg2.connect(
        dbname="ranking",
        user="postgres",
        password="520555",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()

    # 执行查询
    #cursor.execute("SELECT id,name,level,city,province,rating_f,ranking_f FROM schools ORDER BY rating_f NULLS LAST")
    cursor.execute("SELECT id, name, level, city, province, rating_f, ranking_f FROM schools WHERE level = 'Secondary' AND province = 'ON' ORDER BY COALESCE(rating_f, -1) DESC, rating_f")
    schools = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 将查询结果传递给模板
    context = {
        'schools': schools
    }
    return render(request, 'index.html', context)

def ele_BC_schools(request):
    conn = psycopg2.connect(
        dbname="ranking",
        user="postgres",
        password="520555",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()

    # 执行查询
    #cursor.execute("SELECT id,name,level,city,province,rating_f,ranking_f FROM schools ORDER BY rating_f NULLS LAST")
    cursor.execute("SELECT id, name, level, city, province, rating_f, ranking_f FROM schools WHERE level = 'Elementary' AND province = 'BC' ORDER BY COALESCE(rating_f, -1) DESC, rating_f")
    schools = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 将查询结果传递给模板
    context = {
        'schools': schools
    }
    return render(request, 'schools/elementaryschool_BC.html', context)

def ele_ON_schools(request):
    conn = psycopg2.connect(
        dbname="ranking",
        user="postgres",
        password="520555",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()

    # 执行查询
    #cursor.execute("SELECT id,name,level,city,province,rating_f,ranking_f FROM schools ORDER BY rating_f NULLS LAST")
    cursor.execute("SELECT id, name, level, city, province, rating_f, ranking_f FROM schools WHERE level = 'Elementary' AND province = 'ON' ORDER BY COALESCE(rating_f, -1) DESC, rating_f")
    schools = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 将查询结果传递给模板
    context = {
        'schools': schools
    }
    return render(request, 'schools/elementaryschool_ON.html', context)


def sec_BC_schools(request):
    conn = psycopg2.connect(
        dbname="ranking",
        user="postgres",
        password="520555",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()

    # 执行查询
    #cursor.execute("SELECT id,name,level,city,province,rating_f,ranking_f FROM schools ORDER BY rating_f NULLS LAST")
    cursor.execute("SELECT id, name, level, city, province, rating_f, ranking_f FROM schools WHERE level = 'Secondary' AND province = 'BC' ORDER BY COALESCE(rating_f, -1) DESC, rating_f")
    schools = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 将查询结果传递给模板
    context = {
        'schools': schools
    }
    return render(request, 'schools/secondaryschool_BC.html', context)


def search(request):
    name = request.GET.get('keywords', '')
    province = request.GET.get('province','')
    city = request.GET.get('city', '')
    min_rating = request.GET.get('min_rating', '')

    conn = psycopg2.connect(
        dbname="ranking",
        user="postgres",
        password="520555",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()

    params = []
    conditions = []

    # 构建 SQL 查询条件
    if name:
        conditions.append("name ILIKE %s")
        params.append("%" + name + "%")
    if province:
        conditions.append("province ILIKE %s")
        params.append("%" + province + "%")
    if city:
        conditions.append("city ILIKE %s")
        params.append("%" + city + "%")
    if min_rating:
        conditions.append("rating_f >= %s")
        params.append(min_rating)

    # 构建完整的 SQL 查询语句
    query = """
        SELECT id, name, level, city, province, rating_f, ranking_f 
        FROM schools 
        """

    if conditions:
        query += "WHERE " + " AND ".join(conditions)

    query += " ORDER BY COALESCE(rating_f, -1) DESC, rating_f"

    # 执行带有参数的 SQL 查询
    cursor.execute(query, params)
    schools = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    context = {
        'schools': schools,
        'query': query,
    }
    return render(request, 'schools/search.html', context)


def get_cities(request):
    province = request.GET.get('province')
    cities = []
    if province == 'BC':
        cities = [
            {'value': 'Vancouver', 'text': '温哥华'},
            {'value': 'Victoria', 'text': '维多利亚'},
            {'value': 'Richmond', 'text': '列治文'},
            {'value': 'Surrey', 'text': '素里'},
            {'value': 'Burnaby', 'text': '本拿比'},
            {'value': 'Kelowna', 'text': '基隆拿'},
            {'value': 'Abbotsford', 'text': '阿伯茨福德'},
            {'value': 'Coquitlam', 'text': '高贵林'},
            {'value': 'Nanaimo', 'text': '纳奈莫'},
            {'value': 'Kamloops', 'text': '坎卢普斯'},
            {'value': 'Chilliwack', 'text': '奇利瓦克'},
            {'value': 'Prince George', 'text': '乔治王子城'},
            {'value': 'New Westminster', 'text': '新威斯敏斯特'}
        ]
    elif province == 'ON':
        cities = [
            {'value': 'Toronto', 'text': '多伦多'},
            {'value': 'Ottawa', 'text': '渥太华'},
            {'value': 'Mississauga', 'text': '米西索加'},
            {'value': 'Brampton', 'text': '布兰普顿'},
            {'value': 'Hamilton', 'text': '汉密尔顿'},
            {'value': 'London', 'text': '伦敦'},
            {'value': 'Markham', 'text': '万锦'},
            {'value': 'Vaughan', 'text': '旺市'},
            {'value': 'Kitchener', 'text': '基奇纳'},
            {'value': 'Windsor', 'text': '温莎'},
            {'value': 'Richmond Hill', 'text': '列治文山'},
            {'value': 'Barrie', 'text': '巴里'},
            {'value': 'Guelph', 'text': '圭尔夫'},
            {'value': 'Kingston', 'text': '金斯顿'},
            {'value': 'Thunder Bay', 'text': '桑德贝'},
            {'value': 'Waterloo', 'text': '滑铁卢'}
        ]
    return JsonResponse({'cities': cities})
