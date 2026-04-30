import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="1234567890"
)

cur = conn.cursor()


def get_or_create_user(username):
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    user = cur.fetchone()

    if user:
        return user[0]

    cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
    conn.commit()
    return cur.fetchone()[0]


def save_score(username, score, level):
    user_id = get_or_create_user(username)

    cur.execute(
        "INSERT INTO game_sessions(player_id, score, level_reached) VALUES(%s,%s,%s)",
        (user_id, score, level)
    )
    conn.commit()


def get_top_scores():
    cur.execute("""
        SELECT p.username, g.score, g.level_reached
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC
        LIMIT 10
    """)
    return cur.fetchall()