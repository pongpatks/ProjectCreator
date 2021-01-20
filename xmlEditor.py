import datetime
import os
import shutil
from xml.etree import ElementTree as ET

projectTemplatePath = "Y:\\MAYA\\SCRIPTS\\openPipeline2\\projectTemplate.xml"
projectListPath = "Y:\\MAYA\\SCRIPTS\\openPipeline2\\openPipeline_projects.xml"

def backupProjectXml():
    """"""
    openPipelineDir = projectListPath.rsplit('\\', 1)[0]
    todayBackupFile = "".join([openPipelineDir, "\\_BAK", '\\openPipeline_projects_', str(datetime.date.today()), ".xml"])
    print(todayBackupFile)
    try:
        shutil.copy2(projectListPath, todayBackupFile)
    except:
        return False

    return True

def appendNewProject(overrideDict={}):
    """"""
    # Read project template as xml element
    projTemplate = ET.parse(projectTemplatePath)

    # if there is override dict, find the corresponding xml elements, replace them with the override dict values
    root = projTemplate.getroot()
    if overrideDict:
        for each in overrideDict:
            elem = root.find(each)
            elem.text = overrideDict[each]

    projString = ET.tostring(root, encoding='unicode')
    # Read ALL project list as text file
    f = open(projectListPath, "r")
    lines = f.readlines()
    f.close()

    # Find the end of file line
    eofIndex = 0
    eofString = "</openPipeline_project_list>"

    for i in range(-1, -10, -1):
        if eofString in lines[i]:
            eofIndex = i
            break

    # Write file back
    if eofIndex != 0:
        f = open(projectListPath, "w")

        newText = "".join(lines[:eofIndex])
        f.write("".join([newText, '    ', projString, '\n', eofString]))
        f.close()
    else:
        raise AssertionError("Read file error. XML end scope is missing.")
        return False

    return True