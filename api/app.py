import mysql.connector
import configDB
from osuAPI import osuAPI
from flask import Flask, jsonify, request
from flask_cors import CORS

#Configuration
DEBUG = True

#Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, ressources={r'/*': {'origins': '*'}})

#check route

@app.route('/', methods=['GET'])
def root():
    return "It works :)"

@app.route("/register", methods=['POST'])
def register():
    response_object = {'status': 'Insert Succeed'}
    userInfos = request.get_json(force=True)
    playerUsername = userInfos.get('username')
    playersExist = checkIfPlayerAlreadyRegistered(playerUsername)
    if playersExist:
        return "{\"statusText: Already registered}", 400
    osuUser = osuAPI.getUser(playerUsername)
    db = connection()
    cursor = db.cursor()
    sql = "INSERT INTO Player(osu_id, pseudo, pp, player_rank, discordTag) VALUES (%s,%s,%s, %s, %s)"
    try:
        dataToInsert = (int(osuUser['user_id']), osuUser['username'], float(osuUser['pp_raw']), int(osuUser['pp_rank']), userInfos['discord'])
        cursor.execute(sql, dataToInsert)
        db.commit()
        db.close()
        return "Status :"+response_object.get('status')
    except mysql.connector.Error as error:
        print("Failed to insert : {}".format(error))
        db.rollback()
        response_object['status'] = 'Insert failed'
        db.close()
        return "Status : "+response_object.get('status')

@app.route("/players", methods=['GET'])
def playersList():
    playersListing = getPlayerList()
    if playersListing:
        L = []
        for player in playersListing:
            L.append({"username": player['pseudo'], "pp": player['pp'], "rank": player['rank'], "osu_id": player['osu_id']})
        return jsonify(L), 200
    else:
        return "{\"statusText\": \"No player registered\"}", 200

@app.route("/registerTeams", methods=['POST'])
def registerTeams():
    teamsToInsert = request.get_json(force=True)
    teams = teamsToInsert.get('teams')
    for team in teams:
        insT = insertTeam(team['teamName'])
        instPs = insertPlayersInTeam(team)
        if not insT or not instPs:
            return "Team registration failed :\n insertTeam = "+str(insT)+", insertPlayersInTeam = "+str(instPs), 400
    return "Teams has been saved on database", 200 

@app.route("/teams", methods=['GET'])
def teamsList():
    teamsListing = getTeamsList()
    if teamsListing:
        return jsonify(teamsListing), 200
    else:
        return "{\"statusText\": \"No team created\"}", 200

def connection():
    db = mysql.connector.connect(host=configDB.HOST,
                        user=configDB.USER,
                        password=configDB.PASSWORD,
                        database=configDB.DATABASE,
                        auth_plugin='mysql_native_password')
    return db

def getPlayerList():
    db = connection()
    sql = "SELECT * FROM player"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        rawPlayers = cursor.fetchall()
        players = []
        for player in rawPlayers:
            players.append({"osu_id": player[0], "pseudo": player[2], "pp": player[3], "rank": player[4], "discordTag": player[5]})
        return players
    except:
        return []

def checkIfPlayerAlreadyRegistered(username):
    playersList = getPlayerList()
    if playersList:
        playerExist = False
        for player in playersList:
            if player['pseudo'] == username:
                playerExist = True
                break
        return playerExist
    else:
        return False

def insertTeam(teamName):
    db = connection()
    cursor = db.cursor()
    sql = "INSERT INTO Team(team_name) VALUES (%s)"
    try:
        cursor.execute(sql, (teamName,))
        db.commit()
        db.close()
        return True
    except mysql.connector.Error as error:
        print("Failed to insert : {}".format(error))
        db.rollback()
        db.close()
        return False

def insertPlayersInTeam(team):
    db = connection()
    cursor = db.cursor(buffered=True)
    sqlGetTeamId = "SELECT team_id FROM team WHERE team_name=%s"
    teamId = 0
    try: 
        cursor.execute(sqlGetTeamId, (team['teamName'],))
        db.commit()
        teamId = cursor.fetchall()[0][0]
    except mysql.connector.Error as error:
        print("Failed to get id : {}".format(error))
        db.rollback()
        db.close()
        return False
    sqlUpdatePlayer = "UPDATE Player SET team_id=%s, qualifier_score=%s WHERE osu_id=%s"
    for player in team['players']:
        try:
            cursor.execute(sqlUpdatePlayer, (teamId, player['osu_id'], player['qualifier_score'],))
            db.commit()
        except mysql.connector.Error as error:
            print("Failed to update : {}".format(error))
            db.rollback()
            db.close()
            return False
    db.close()
    return True

def getTeamsList():
    db = connection()
    cursor = db.cursor(buffered=True)
    teamNames = []
    sqlGetTeamNames = "SELECT team_name FROM Team"
    try:
        cursor.execute(sqlGetTeamNames)
        db.commit()
        teamNames = cursor.fetchall() 
    except mysql.connector.Error as error:
        print("Failed to get team names : {}".format(error))
        db.rollback()
        db.close()
        return []
    sqlGetTeams = "SELECT osu_id, pseudo, qualifier_score, player_rank FROM Player INNER JOIN Team ON Player.team_id=Team.team_id WHERE Team.team_name=%s ORDER BY qualifier_score DESC"
    teams = []
    for teamName in teamNames:
        try:
            cursor.execute(sqlGetTeams, (teamName[0],))
            db.commit()
            rawTeam = cursor.fetchall()
            players = []
            for player in rawTeam:
                players.append({"username": player[1], "osu_id": player[0], "qualifier_score": player[2], "rank": player[3]})
            teams.append({"team_name": teamName[0], "players": players})
        except mysql.connector.Error as error:
            print("Failed to get teams : {}".format(error))
            db.rollback()
            db.close()
            return []
    db.close()
    return teams

if __name__ == '__main__':
    app.run()
