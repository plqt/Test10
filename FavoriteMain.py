import pymysql

conn = pymysql.connect(
                    user='admin',
                    passwd='10pan',
                    db='cook',
                    port = 3306,
                    charset = 'utf8'
)

cur = conn.cursor()
cur.execute('USE cook')

def FavoriteRegister(userID,recipeURL,recipeTitle):
    cur.execute('SELECT * FROM favorite WHERE userID = %s'
               'AND recipeURL = %s'
               'AND recipeTitle = %s',(userID, recipeURL, recipeTitle))

    if cur.rowcount == 0 :
        cur.execute('INSERT INTO favorite (userID,recipeURL,recipeTitle) VALUES (%s,%s,%s)',(userID, recipeURL, recipeTitle))
        conn.commit()
        return 1

    return 0

def FavoriteDisplay(userID):
    favoriteTitles = []
    cur.execute('SELECT * FROM favorite WHERE UserID = %s', (userID))
    favoriteTitles = [row[2] for row in cur.fetchall()]
    return favoriteTitles

def FavoriteDelete(userID,recipeTitle):
    cur.execute('DELETE * FROM favorite WHERE UserID = %s'
               'AND recipeTitle = %s',(userID, recipeTitle))
    conn.commit()