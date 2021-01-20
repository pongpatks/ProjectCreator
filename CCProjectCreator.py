#---------------------------------------------------------------------------------------------------------------------------------------------
# My Liaison Project Creator
# Version 0.5.0
# 
# Pongpat Sombatpanich (Kun) - 3/07/2017
# Change log
# 0.5.0 - add a function which will modify openPipeline xml file for the tool project setup.
#
#---------------------------------------------------------------------------------------------------------------------------------------------
# Burak Ertekin - 26/02/2016
# 0.2.1 - added input/output file synchronization feature for color grading tab
# 0.2.2 - added audio and artworks buttons for grading
# 0.2.3 - forResolve feature added
# 0.2.4 - first grade feature added
# 0.3.4 - color grading tab replaced by archiving tab
# 0.3.5 - if no project found in directory don't give any error. just show no projects.
# 0.3.6 - filtering out the folder lists with hidden directories
# 0.3.7 - archive error fixed with empty sequence and shot lists
# 0.4.0 - changed tool name for Cherry Cherry to My Liaison
#---------------------------------------------------------------------------------------------------------------------------------------------

# Import python modules
import sys
import os
from datetime import date

# Import GUI modules
from PyQt4 import QtCore, QtGui

# Import utility modules
from FolderCreator import FolderCreator
from openPipelineIntegration import xmlEditor

from Ui_CCProjectCreator import Ui_CCProjectCreator

serverPath = 'M:/JOBS/'
emptyDirectory = False

def openPipelineNewProject(projName, projPath):
    """"""
    today = date.today()
    #let's just say a month later
    deadlineDate = today.replace(year=today.year+1)

    newProjectParams = {'name': projName,
                        'path': projPath,
                        'description': projName,
                        'date': today.strftime("%m/%d/%Y"),
                        'deadline': deadlineDate.strftime("%m/%d/%Y")}

    return xmlEditor.appendNewProject(newProjectParams)



class CCProjectCreator(QtGui.QMainWindow, Ui_CCProjectCreator, FolderCreator):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.folderCreator = FolderCreator()
        emptyDirectory = False
        self.fillComboBoxes()

        if self.getJobList():
            self.getSequenceList()

        #button connections of UI
        self.connect(self.button_structure, QtCore.SIGNAL('clicked()'), self.createStructure)
        self.connect(self.button_createSequence, QtCore.SIGNAL('clicked()'), self.createSequence)
        self.connect(self.button_browseConfig, QtCore.SIGNAL('clicked()'), self.browseConfig)
        self.connect(self.button_addShots, QtCore.SIGNAL('clicked()'), self.addShots)
        self.connect(self.button_updateConfig, QtCore.SIGNAL('clicked()'), self.updateConfig)
        self.connect(self.button_archive, QtCore.SIGNAL('clicked()'), self.archive)

        if self.getJobList():
            #updating combo boxes
            self.jobNameComboBox_2.activated['QString'].connect(self.getSequenceList)
            self.archiveProjectComboBox.activated['QString'].connect(self.getArchiveSequenceList)
            self.archiveSequenceComboBox.activated['QString'].connect(self.getArchiveShotList)

    def fillComboBoxes(self):
        #add job list
        self.jobNameComboBox.clear()
        self.jobNameComboBox.addItems(self.getJobList())
        self.jobNameComboBox_2.clear()
        self.jobNameComboBox_2.addItems(self.getJobList())
        self.jobNameComboBox_3.clear()
        self.jobNameComboBox_3.addItems(self.getJobList())
        self.archiveProjectComboBox.clear()
        self.archiveProjectComboBox.addItems(self.getJobList())

        if self.getJobList():
            #fill sequence combo boxes as well
            self.getSequenceList()
            self.getArchiveSequenceList()
            self.getArchiveShotList()

    def getJobList(self):
        #get folder list
        joblist = [d for d in os.listdir(serverPath) if os.path.isdir(os.path.join(serverPath, d))]
        #cleaning the list from hidden
        joblist = self.noHiddenDir(joblist)
        return joblist

    def getSequenceList(self):
        projectName = str(self.jobNameComboBox_2.currentText())
        newPath = serverPath + projectName + "/__Sequences/"
        #get sequence folder list
        sequencelist = [d for d in os.listdir(newPath) if os.path.isdir(os.path.join(newPath, d))]
        #cleaning the list from hidden
        sequencelist = self.noHiddenDir(sequencelist)
        #clear existing combo box and add new items
        self.sequenceNameComboBox.clear()
        self.sequenceNameComboBox.addItems(sequencelist)

    def getArchiveSequenceList(self):
        projectName = str(self.archiveProjectComboBox.currentText())
        newPath = serverPath + projectName + "/__Sequences/"
        #get sequence folder list
        sequencelist = [d for d in os.listdir(newPath) if os.path.isdir(os.path.join(newPath, d))]
        #cleaning the list from hidden
        sequencelist = self.noHiddenDir(sequencelist)

        if not sequencelist:
            QtGui.QMessageBox.information(self, 'Error!', 'No sequences found for this project', QtGui.QMessageBox.Ok)
            self.archiveSequenceComboBox.clear()
        else:
            #refresh the combo box according to the project
            self.archiveSequenceComboBox.clear()
            self.archiveSequenceComboBox.addItems(sequencelist)
            #update for shot combo box
            newPath = serverPath + projectName + "/__Sequences/" + sequencelist[0]
            #get shot folder list
            shotlist = [d for d in os.listdir(newPath) if os.path.isdir(os.path.join(newPath, d))]
            #cleaning the list from hidden
            shotlist = self.noHiddenDir(shotlist)
            #refresh the combo box according to the sequence and project
            self.archiveShotComboBox.clear()
            self.archiveShotComboBox.addItems(shotlist)
            self.archiveShotComboBox.addItem('ALL')

    def getArchiveShotList(self):
        projectName = str(self.archiveProjectComboBox.currentText())
        sequenceName = str(self.archiveSequenceComboBox.currentText())
        newPath = serverPath + projectName + "/__Sequences/" + sequenceName
        #get shot folder list
        shotlist = [d for d in os.listdir(newPath) if os.path.isdir(os.path.join(newPath, d))]
        #cleaning the list from hidden
        shotlist = self.noHiddenDir(shotlist)

        if not shotlist:
            QtGui.QMessageBox.information(self, 'Error!', 'No shots found for this project', QtGui.QMessageBox.Ok)
            self.archiveShotComboBox.clear()
        else:
            #refresh the combo box according to the sequence and project
            self.archiveShotComboBox.clear()
            self.archiveShotComboBox.addItems(shotlist)
            self.archiveShotComboBox.addItem('ALL')

    def createStructure(self):
        #get the project name from line edit
        jobName = self.jobNameLineEdit.text().toUtf8()
        if jobName == "":
            #if its an empty string, display an error message
            QtGui.QMessageBox.information(self, 'Error!', 'Invalid name for a project!', QtGui.QMessageBox.Ok)
        else:
            if self.onlyAscii(jobName):
                jobName = jobName.upper()
                if jobName in self.getJobList():
                    QtGui.QMessageBox.information(self, 'Error!', 'This project already exists!')
                else:
                    jobName = jobName.toUpper()
                    jobPath = serverPath + jobName
                    jobPath = str(jobPath)
                    #create the main folder structure and print success message
                    #CONGRATS
                    #using big copy tree function. sending empty strings for sequence and shot names to not create
                    #_sequenceDb and _shotDb folders
                    self.folderCreator.copyTreeBig(self.folderCreator.templatePath(sys.argv[0]), jobPath, "", "")
                    msg = 'You have created the project ' + jobName
                    QtGui.QMessageBox.information(self, 'Success!', str(msg), QtGui.QMessageBox.Ok)

                    result = openPipelineNewProject(str(jobName), jobPath+'/MAYA')

                    if result is False:
                        QtGui.QMessageBox.information(self, 'Warning', 'Failed to setup new project for OpenPipeline. The tool might not be working correctly.')

                    self.fillComboBoxes()
            else:
                QtGui.QMessageBox.information(self, 'Error!', 'Invalid input! You can only use English characters, numbers or underscore!')

    def createSequence(self):
        #get the project name from the combo box
        projectName = self.jobNameComboBox_2.currentText().toUtf8()
        #get path of the project
        projectPath = serverPath + "/" + projectName
        #dummy sequence path to check overlapping sequence names
        sequencePath = projectPath + "/__Sequences"
        #get the string located in sequence name line edit
        sequenceName = self.sequenceNameLineEdit.text().toUtf8()
        #to check if sequence is existing
        newPath = serverPath + projectName + "/__Sequences/"
        #get sequence folder list
        sequencelist = [d for d in os.listdir(newPath) if os.path.isdir(os.path.join(newPath, d))]
        #cleaning the list from hidden
        sequencelist = self.noHiddenDir(sequencelist)
        if " " in sequenceName:
            #if sequence name has space, throw an error
            QtGui.QMessageBox.information(self, 'Error!', 'No spaces allowed for sequence names', QtGui.QMessageBox.Ok)
        elif not sequenceName:
            #if sequence name is empty
            QtGui.QMessageBox.information(self, 'Error!', 'Enter a name for sequence', QtGui.QMessageBox.Ok)
        else:
            if self.onlyAscii(sequenceName):
                #if sequenceName in sequencelist:
                #	QtGui.QMessageBox.information(self, 'Error!', 'This sequence already exists!')
                #else:
                    #if its a proper sequence name, call add shots function since tab number 2 creates sequences with/without shots
                self.addShots()
            else:
                QtGui.QMessageBox.information(self, 'Error!', 'Invalid input! You can only use English characters, numbers or underscore!')

    def browseConfig(self):
        #opening a qfiledialog to browse folders for configuration folders
        configPath = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory", "//serverraid02/cherrytechnic$/SHOTGUN/main_config/config/"))
        self.configLocationLineEdit.setText(configPath)

    def addShots(self):
        #get the current tab info
        index = self.tabWidget.currentIndex()
        if index == 1:
            #we are in create sequence tab
            projectName = self.jobNameComboBox.currentText().toUtf8()
            #get path of the project
            projectPath = serverPath + "/" + projectName
            #get the sequence name you want to create the shots from combo box
            sequenceName = self.sequenceNameLineEdit.text().toUtf8()
            #shot number text
            shotNumText = self.shotNumbersLineEdit.text().toUtf8()
            if not shotNumText:
                #if shot number text is empty
                inpCheck = QtGui.QMessageBox.critical(self, 'Error!', 'You are creating a Sequence with no Shots. \n Press OK to continue, Cancel to abort', QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
                if inpCheck == QtGui.QMessageBox.Ok:
                    #just create sequence
                    sequenceName = sequenceName.toUpper()
                    self.folderCreator.createSequence(sequenceName, projectPath)
                    self.getSequenceList()
                    msg = 'You have created the sequence ' + sequenceName
                    QtGui.QMessageBox.information(self, 'Success!', str(msg), QtGui.QMessageBox.Ok)
                else:
                    #pressed cancel so don't do anything
                    pass
            else:
                #there is an input for shot numbers therefore create a sequence and add shots to it
                sequenceName = sequenceName.toUpper()
                self.folderCreator.createSequence(sequenceName, projectPath)
                #update sequence list
                self.getSequenceList()
                #input check the shot list
                shotlist = self.shotInputCheck(shotNumText, sequenceName, projectName)
                #cleaning the list from hidden
                shotlist = self.noHiddenDir(shotlist)
                if shotlist is not None:
                    #create shot folders
                    self.folderCreator.createShots(sequenceName, shotlist, projectPath)
                    msg = ""
                    if len(shotlist) > 1:
                        msg = 'You have created shots ' + shotlist[0] + '-' + shotlist[len(shotlist)-1]
                    else:
                        msg = 'You have created the shot ' + shotlist[0]
                    QtGui.QMessageBox.information(self, 'Success!', str(msg), QtGui.QMessageBox.Ok)
                else:
                    #some error at input check
                    pass

        elif index == 2:
            #we are in add shots tab
            projectName = self.jobNameComboBox_2.currentText().toUtf8()
            #get path of the project
            projectPath = serverPath + "/" + projectName
            sequenceName = self.sequenceNameComboBox.currentText().toUtf8()
            sequenceName = sequenceName.toUpper()
            #shot number text
            shotNumText = self.shotNumbersLineEdit_2.text().toUtf8()
            if not shotNumText:
                #empty string therefore hit a warning
                QtGui.QMessageBox.information(self, 'Error!', 'No input is given. Write the Shots you want to add to the Sequence', QtGui.QMessageBox.Ok)
            else:
                #make an input check
                shotlist = self.shotInputCheck(shotNumText, sequenceName, projectName)
                #cleaning the list from hidden
                shotlist = self.noHiddenDir(shotlist)
                if shotlist is not None:
                    #create shot folders
                    self.folderCreator.createShots(sequenceName, shotlist, projectPath)
                    msg = ""
                    if len(shotlist) > 1:
                        msg = 'You have created shots ' + shotlist[0] + '-' + shotlist[len(shotlist)-1]
                    else:
                        msg = 'You have created the shot ' + shotlist[0]
                    QtGui.QMessageBox.information(self, 'Success!', str(msg), QtGui.QMessageBox.Ok)
                else:
                    #some error at input check
                    pass
        else:
            #we are somewhere else therefore don't do anything
            pass

    def shotInputCheck(self, inputStr, sequenceName, projectName):
        if self.onlyNumbers(inputStr):
            #our input check is good to go! for a list of shots
            if "-" in inputStr:
                #if this is a list of shots
                templist = inputStr.split("-")
                #first and last elements of the list
                first = templist[0]
                last = templist[len(templist)-1]
                if not first or not last:
                    QtGui.QMessageBox.information(self, 'Error!', 'Invalid list. There should be Shot numbers at both ends of the dash', QtGui.QMessageBox.Ok)
                else:
                    #creating a list for shots to return
                    shotPath = serverPath + projectName + "/__Sequences/" + sequenceName + "/"
                    checklist = [d for d in os.listdir(shotPath) if os.path.isdir(os.path.join(shotPath, d))]
                    #cleaning the list from hidden
                    checklist = self.noHiddenDir(checklist)
                    shotlist = []
                    first = int(first)
                    last = int(last)
                    if first>last:
                        #temp list is decrementing
                        diff = (first - last) + 1
                        for i in range(diff):
                            tempValue = last + i
                            shotlist.append("SH"+str(tempValue))
                        #if any(value in checklist for value in shotlist):
                            #if the shot list given as input exists, throw and error and don't return
                            #QtGui.QMessageBox.information(self, 'Error!', 'This Shot list already exists.', QtGui.QMessageBox.Ok)
                        #else:
                        return shotlist
                    elif first == last:
                        #add only one and return
                        shotlist.append("SH"+str(first))
                        #if any(value in checklist for value in shotlist):
                            #if the shot list given as input exists, throw and error and don't return
                            #QtGui.QMessageBox.information(self, 'Error!', 'This Shot list already exists.', QtGui.QMessageBox.Ok)
                        #else:
                        return shotlist
                    else:
                        #temp list is incrementing
                        diff = (last - first) + 1
                        for i in range(diff):
                            tempValue = first + i
                            shotlist.append("SH"+str(tempValue))
                        #if any(value in checklist for value in shotlist):
                            #if the shot list given as input exists, throw and error and don't return
                            #QtGui.QMessageBox.information(self, 'Error!', 'This Shot list already exists.', QtGui.QMessageBox.Ok)
                        #else:
                        return shotlist
            else:
                #if this is a single shot, compute the current shot path and check if the shot already exists
                shotPath = serverPath + projectName + "/__Sequences/" + sequenceName + "/"
                checklist = [d for d in os.listdir(shotPath) if os.path.isdir(os.path.join(shotPath, d))]
                #if "SH"+inputStr in checklist:
                    #QtGui.QMessageBox.information(self, 'Error!', 'This Shot already exists', QtGui.QMessageBox.Ok)
                #else:
                    #creating a list to maintain stability and return the only element in a list
                shotlist = []
                shotlist.append("SH"+inputStr)
                return shotlist

        elif self.onlyNumbersLetters(inputStr):
            #our input check is good to go! for single shots(with letters)
            shotPath = serverPath + projectName + "/__Sequences/" + sequenceName + "/"
            checklist = [d for d in os.listdir(shotPath) if os.path.isdir(os.path.join(shotPath, d))]
            inputStr = inputStr.toUpper()

            #if "SH"+inputStr in checklist:
                #QtGui.QMessageBox.information(self, 'Error!', 'This Shot already exists', QtGui.QMessageBox.Ok)
            #else:
            shotlist = []
            shotlist.append("SH"+inputStr)
            return shotlist

        else:
            QtGui.QMessageBox.information(self, 'Error!', 'Invalid input! You can only use numbers and dash if you want to create a LIST of Shots.\nYou can use letters when creating a single Shot', QtGui.QMessageBox.Ok)

    def updateConfig(self):
        #get the path from line edit
        path = self.configLocationLineEdit.text().toUtf8()
        if os.path.exists((path+"/cache") and (path+"/config") and (path+"/install")):
            destJob = self.jobNameComboBox_3.currentText().toUtf8()
            dest = serverPath + destJob + "/_Edit/SHOTGUN/config"
            source = path
            print("dest: " + dest)
            print("source: " + source)

            self.folderCreator.copyTreeConfig(source, dest)
            QtGui.QMessageBox.information(self, 'Success!', 'You have succesfully copied Shotgun configuration folder!', QtGui.QMessageBox.Ok)

    def archive(self):
        #get the project name from the combo box
        projectName = self.archiveProjectComboBox.currentText().toUtf8()
        #get the sequence name from the combo box
        sequenceName = self.archiveSequenceComboBox.currentText().toUtf8()
        #get the shot name to check whether to make a single or a bundle clean
        shotName = self.archiveShotComboBox.currentText().toUtf8()

        #if we will make a bundle clean
        if shotName == 'ALL':
            newPath = serverPath + projectName + "/__Sequences/" + sequenceName
            #get shot folder list
            shotlist = [d for d in os.listdir(newPath) if os.path.isdir(os.path.join(newPath, d))]
            #cleaning the list from hidden
            shotlist = self.noHiddenDir(shotlist)
            for item in shotlist:
                self.cleaner(projectName, sequenceName, item)
        #if we pick a single shot
        else:
            self.cleaner(projectName, sequenceName, shotName)

    def cleaner(self, projectName, sequenceName, shotName):
        #directory path for shot to be cleaned
            dirpath = serverPath + projectName + "/__Sequences/" + sequenceName + "/" + shotName + "/_Comp/Outputs/"
            import re
            #regular expression to filter out only the version directories
            regex = re.compile(r'(v[0-9]+)')

            # full subdirectory listdir
            folder_list = []
            folder_list = os.listdir(dirpath)

            # filtered list. just versions here
            folder_list = [i for i in folder_list if regex.match(i)]

            # new list for 5 recent versions and deleting list
            recent_list = []
            delete_list = []

            # length of the folder list for readability
            length = len(folder_list)

            #if the number of versions inside the directory is greater than 5 than go for cleaning
            if length > 5:
                # get the last 5 versions
                for i in range(length-5, length):
                    recent_list.append(folder_list[i])

                #string of the versions to be kept
                recent_list_str = ''
                for i in recent_list:
                    recent_list_str += i + ', '

                for i in folder_list:
                    # string of the path of each directory to be searched
                    searchString = os.path.join(dirpath, i)

                    for j in recent_list:
                        if j not in searchString:
                            #shutil.rmtree(searchString)
                            delete_list.append(i)
                            break
                        else:
                            recent_list.pop(0)
                            break

                #string of versions to be deleted
                delete_list_str = ''
                for i in delete_list:
                    delete_list_str += i + ','

                #message box showing versions to be deleted and to be kept
                msg = 'This is ' + shotName + '\nYou are deleting following versions:\n' + delete_list_str + '\nAnd keeping following folders:\n' + recent_list_str + '\nPress OK to continue, Cancel to abort'
                #input check. if ok then delete. if cancel then don't do anything
                inpCheck = QtGui.QMessageBox.critical(self, 'Warning!', str(msg), QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
                #GREEN LIGHT - DO THE CLEANING
                if inpCheck == QtGui.QMessageBox.Ok:
                    import shutil
                    for item in delete_list:
                        delpath = os.path.join(dirpath, item)
                        #TO TEST
                        #print delpath
                        #!!!! CLEANING !!!! BEWARE !!!!
                        shutil.rmtree(str(delpath))
                #pressed cancel so don't do anything
                else:
                    pass
            else:
                pass

    def noHiddenDir(self, input_list):
        #regular expression to filter out folders with .
        import re
        regex = re.compile(r'\.(.*)')

        # filtered list
        cleanlist = [i for i in input_list if not regex.match(i)]
        # return filtered list
        return cleanlist

    def onlyNumbersLetters(self, str):
        #if the given input string is a number and/or string value
        return all(48<=ord(c)<=57 or 65<=ord(c)<=90 or 97<=ord(c)<=122 for c in str)

    def onlyNumbers(self, str):
        #if the given input string is a number or dash
        return all(48<=ord(c)<=57 or ord(c)==45 for c in str)

    def onlyAscii(self, str):
        #if the given input string is lower case, upper case chars, numbers or underscore; return true
        return all(97<=ord(c)<=122 or 65<=ord(c)<=90 or 48<=ord(c)<=57 or ord(c)==95 for c in str)

def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = CCProjectCreator()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()