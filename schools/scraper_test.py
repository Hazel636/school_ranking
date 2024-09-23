from bs4 import BeautifulSoup
import psycopg2
from new_table import create_schools_table

create_schools_table()

html_file_path = 'html_files/Fraser_Secondary_ON.html'
with open(html_file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有<tr>标签，这些标签代表每一行数据
rows = soup.find_all('tr')

try:
    conn = psycopg2.connect(
        dbname="ranking",  # 数据库名
        user="postgres",  # 数据库用户名
        password="520555",  # 数据库密码
        host="localhost",  # 数据库主机地址
        port="5433",
    )
    cursor = conn.cursor()

    for row in rows:
        td_elements = row.find_all('td')

        if not td_elements:
            continue

        city_td = td_elements[3]  # 这里假设城市信息在第1列
        if city_td:
            city = city_td.text.strip()
        else:
            city = "N/A"

        ranking_td = td_elements[2]
        if ranking_td:
            ranking = ranking_td.text.strip()
        else:
            ranking = "N/A"

        school_name = row.find('td', class_='school-name text-xs-left')
        if school_name:
            name = school_name.text.strip()
            link_a = school_name.find('a')
            if link_a:
                link = link_a['href']
        else:
            name = "N/A"
            link = "N/A"
        
        rating_color_3 = row.find('td', class_='school-rating text-xs-center score_color_3')
        rating_color_4 = row.find('td', class_='school-rating text-xs-center score_color_4')
        if rating_color_3:
            rating = rating_color_3.text.strip()
        elif rating_color_4:
            rating = rating_color_4.text.strip()
        else:
            rating = None

        insert_query = "INSERT INTO schools (name, level, city, province, address, rating_f, ranking_f, link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (name, 'Secondary', city, 'ON', None, rating, ranking, link))
        conn.commit()

except psycopg2.Error as e:
    print(f"Error inserting data into PostgreSQL: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()
