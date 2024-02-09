
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.myparent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(192, 53)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(218, 110)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(129, 217)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(376, 197)
		self._button1.TabIndex = 1
		self._button1.Text = "Show Home Form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(629, 487)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.FormClosing += self.Form1FormClosing
		self.Load += self.Form1Load
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.myparent.Show()

	def Form1Load(self, sender, e):
		self._label1.Text = self.msg

	def Form1FormClosing(self, sender, e):
		self.myparent.Show()