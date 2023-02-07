import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(322, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(517, 53)
		self._textBox1.TabIndex = 13
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(322, 214)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(517, 77)
		self._label3.TabIndex = 12
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 214)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(265, 77)
		self._label2.TabIndex = 11
		self._label2.Text = "Anagrams?"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(251, 53)
		self._label1.TabIndex = 10
		self._label1.Text = "Enter Word:"
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(613, 327)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(226, 115)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(322, 327)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(226, 115)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 327)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(226, 115)
		self._button1.TabIndex = 7
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(322, 106)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(517, 53)
		self._textBox2.TabIndex = 15
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 109)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(280, 53)
		self._label4.TabIndex = 14
		self._label4.Text = "Enter Word 2:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(851, 464)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "StrInt2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text
		anagram = self._textBox2.Text
		word = word.lower()
		anagram = anagram.lower()
		
		if len(word) != len(anagram):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = anagram.index(c)
				
				if index != -1:
					anagram = anagram[0:index] + anagram[index+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(anagram) == 0)