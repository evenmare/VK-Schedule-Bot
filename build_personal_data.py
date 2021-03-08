from private import connectDB as connectDB

class buildPersonalData:

    tableName = "mainTable"

    dbConnection = connectDB()

    def formattingSelectQuery(self, notFormattedResult):
        formattedResult = []
        for element in notFormattedResult:
            formattedResult.append(element[0])
        return formattedResult

    def selectUserInfo(self, perID):
        operationCursor = self.dbConnection.cursor()
        operationRequest = "SELECT perID, name, eveningNotification, morningNotification, 30minNotification, 5minNotification, localLessons, distantLessons FROM " + buildPersonalData.tableName + " WHERE perID = %s"
        operationValues = (perID, )
        operationCursor.execute(operationRequest, operationValues)
        operationResult = operationCursor.fetchone()
        return operationResult

    def insertNewUserInfo(self, perID, name):
        operationCursor = self.dbConnection.cursor()
        self.deleteUserInfo(perID)
        operationRequest = "INSERT INTO " + buildPersonalData.tableName + " (perID, name, eveningNotification, morningNotification, 30minNotification, 5minNotification, localLessons, distantLessons) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        operationValues = (perID, name, 0, 0, 0, 0, 0, 0)
        operationCursor.execute(operationRequest, operationValues)
        self.dbConnection.commit()

    def updateUserInfo(self, perID, eveningNotification, morningNotification, min30Notification, min5Notification, localLessons, distantLessons):
        operationCursor = self.dbConnection.cursor()
        operationRequest = "UPDATE " + buildPersonalData.tableName + " SET eveningNotification = %s, morningNotification = %s, 30minNotification = %s, 5minNotification = %s, localLessons = %s, distantLessons = %s WHERE perID = %s"
        operationValues = (eveningNotification, morningNotification, min30Notification, min5Notification, localLessons, distantLessons, perID)
        operationCursor.execute(operationRequest, operationValues)
        self.dbConnection.commit()

    def deleteUserInfo(self, perID):
        operationCursor = self.dbConnection.cursor()
        operationRequest = "DELETE FROM " + buildPersonalData.tableName + " WHERE perID = %s"
        operationValues = (perID, )
        operationCursor.execute(operationRequest, operationValues)
        self.dbConnection.commit()

    def selectAllUsers(self):
        operationCursor = self.dbConnection.cursor()
        operationRequest = "SELECT perID FROM " + buildPersonalData.tableName
        operationCursor.execute(operationRequest)
        operationResult = operationCursor.fetchall()
        return self.formattingSelectQuery(operationResult)

    def selectTimeNotifications(self, time_type_of_notification):
        operationCursor = self.dbConnection.cursor()
        operationRequest = "SELECT perID FROM " + buildPersonalData.tableName + " WHERE " + time_type_of_notification + "Notification = 1"
        operationCursor.execute(operationRequest)
        operationResult = operationCursor.fetchall()
        return self.formattingSelectQuery(operationResult)

    def selectLocationNotifications(self, location_type_of_notification):
        operationCursor = self.dbConnection.cursor()
        operationRequest = "SELECT perID FROM " + buildPersonalData.tableName + " WHERE " + location_type_of_notification + "Lessons = 1"
        operationCursor.execute(operationRequest)
        operationResult = operationCursor.fetchall()
        return self.formattingSelectQuery(operationResult)

buildClass = buildPersonalData()