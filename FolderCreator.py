#---------------------------------------------------------------------------------------------------------------------------------------------
#
# Burak Ertekin - 26/02/2016
# Version 0.4.0
# My Liaison Project Creator
# 0.2.1 - added input/output file synchronization feature for color grading tab
# 0.2.2 - added audio and artworks buttons for grading
# 0.3.4 - color grading tab replaced by archiving tab
# 0.4.0 - changed tool name from Cherry Cherry to My Liaison
#
#---------------------------------------------------------------------------------------------------------------------------------------------
import sys
import os
import shutil

serverPath = 'M:/JOBS/'

class FolderCreator(object):
	def copyTreeConfig(self, source, dest, symlinks=False, ignore=None):
		if not os.path.exists(dest):
			os.makedirs(dest)
			
		for item in os.listdir(source):
			s = os.path.join(source, item)
			d = os.path.join(dest, item)

			if os.path.isdir(s):
				self.copyTreeConfig(s, d, symlinks, ignore)
			else:
				if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
					if "pipeline_configuration.yml" not in s:
						if "install_location.yml" not in s:
							shutil.copy2(s, d)

	def copytree(self, source, dest, symlinks=False, ignore=None):
		#retrieved from:
		#http://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
		#using this method instead of built-in copytree of shutil which is kinda buggy

		if not os.path.exists(dest):
			os.makedirs(dest)
		for item in os.listdir(source):
			s = os.path.join(source, item)
			d = os.path.join(dest, item)

			if os.path.isdir(s):
				self.copytree(s, d, symlinks, ignore)
			else:
				if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
					shutil.copy2(s, d)

	def copyTreeBig(self, source, dest, sequenceName, shotName, symlinks=False, ignore=None):
		#main structure copying function
		if not os.path.exists(dest):
			os.makedirs(dest)
		for item in os.listdir(source):
			s = os.path.join(source, item)
			d = os.path.join(dest, item)

			if item == "_sequenceDatabase":
				if sequenceName != "":
					#if we have sequence defined in the list, then continue copying folders etc.
					if os.path.isdir(s):
						self.copyTreeBig(s, d, sequenceName, shotName, symlinks, ignore)
					else:
						if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
							shutil.copy2(s, d)
				else:
					#else pass to next element to copy
					break
			else:
				#if the folder doesn't have any _sequenceDatabase subfolders
				if os.path.isdir(s):
						self.copyTreeBig(s, d, sequenceName, shotName, symlinks, ignore)
				else:
					if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
						shutil.copy2(s, d)

	def copyTreeSeq(self, source, dest, sequenceName, symlinks=False, ignore=None):
		#sequence copying function
		if not os.path.exists(dest):
			os.makedirs(dest)
		for item in os.listdir(source):
			s = os.path.join(source, item)
			d = os.path.join(dest, item)

			if "_sequenceDatabase" in s:
				d = d.replace("_sequenceDatabase", sequenceName)

			if "_shotDatabase" in s:
				#when it finds a _shotDb indicator stop iterating through the function
				#and pass on next element in the list
				break

			if os.path.isdir(s):
				self.copyTreeSeq(s, d, sequenceName, symlinks, ignore)
			else:
				if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
					shutil.copy2(s, d)

	def copyTreeShot(self, source, dest, shotName, sequenceName, symlinks=False, ignore=None):
		#shot copying function
		if not os.path.exists(dest):
			os.makedirs(dest)
		for item in os.listdir(source):
			s = os.path.join(source, item)
			d = os.path.join(dest, item)

			#since shot folder is one level deeper than sequence folder, don't break the loop
			#change folder names according to given inputs
			if "_sequenceDatabase" in s:
				d = d.replace("_sequenceDatabase", sequenceName)

			if "_shotDatabase" in s:
				d = d.replace("_shotDatabase", shotName)

			if os.path.isdir(s):
				self.copyTreeShot(s, d, shotName, sequenceName, symlinks, ignore)
			else:
				if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
					shutil.copy2(s, d)

	def templatePath(self, inp):
		#get the absolute path of the given input and take the corresponding directory
		path = os.path.abspath(inp)
		(head, tail) = os.path.split(path)
		#add template directory to it and return the value
		tempPath = head + "/template"
		return tempPath

	def createSequence(self, sequenceName, projectPath):
		#calling copy sequence folder structure
		#calling only one sequence at a time
		self.copyTreeSeq(self.templatePath(sys.argv[0]), projectPath, sequenceName)

	def createShots(self, sequenceName, shotlist, projectPath):
		#copying shot folders from the main template structure
		#iterate through whole shot list
		for i in range(len(shotlist)):
			self.copyTreeShot(self.templatePath(sys.argv[0]), projectPath, shotlist[i], sequenceName)
