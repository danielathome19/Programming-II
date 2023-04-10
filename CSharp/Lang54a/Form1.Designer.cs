namespace Lang54a
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.lblMiles = new System.Windows.Forms.Label();
            this.lblGallons = new System.Windows.Forms.Label();
            this.lblMpg = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // comboBox1
            // 
            this.comboBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "1970 VW Bug",
            "1979 Firebird",
            "1980 Subaru",
            "1975 Cutlass"});
            this.comboBox1.Location = new System.Drawing.Point(12, 23);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(419, 54);
            this.comboBox1.TabIndex = 0;
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(12, 104);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(419, 66);
            this.button1.TabIndex = 1;
            this.button1.Text = "Calculate";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.Location = new System.Drawing.Point(438, 16);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(203, 66);
            this.button2.TabIndex = 2;
            this.button2.Text = "Clear";
            this.button2.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button3.Location = new System.Drawing.Point(438, 104);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(203, 66);
            this.button3.TabIndex = 3;
            this.button3.Text = "Exit";
            this.button3.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 191);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(220, 87);
            this.label1.TabIndex = 4;
            this.label1.Text = "Miles";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label2
            // 
            this.label2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(12, 291);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(220, 84);
            this.label2.TabIndex = 5;
            this.label2.Text = "Gallons";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label3
            // 
            this.label3.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(12, 390);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(220, 94);
            this.label3.TabIndex = 6;
            this.label3.Text = "Miles Per Gallon";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblMiles
            // 
            this.lblMiles.BackColor = System.Drawing.Color.White;
            this.lblMiles.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblMiles.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblMiles.Location = new System.Drawing.Point(238, 191);
            this.lblMiles.Name = "lblMiles";
            this.lblMiles.Size = new System.Drawing.Size(403, 84);
            this.lblMiles.TabIndex = 7;
            this.lblMiles.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblGallons
            // 
            this.lblGallons.BackColor = System.Drawing.Color.White;
            this.lblGallons.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblGallons.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblGallons.Location = new System.Drawing.Point(238, 291);
            this.lblGallons.Name = "lblGallons";
            this.lblGallons.Size = new System.Drawing.Size(403, 84);
            this.lblGallons.TabIndex = 8;
            this.lblGallons.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblMpg
            // 
            this.lblMpg.BackColor = System.Drawing.Color.White;
            this.lblMpg.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblMpg.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblMpg.Location = new System.Drawing.Point(238, 390);
            this.lblMpg.Name = "lblMpg";
            this.lblMpg.Size = new System.Drawing.Size(403, 94);
            this.lblMpg.TabIndex = 9;
            this.lblMpg.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(654, 503);
            this.Controls.Add(this.lblMpg);
            this.Controls.Add(this.lblGallons);
            this.Controls.Add(this.lblMiles);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.comboBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label lblMiles;
        private System.Windows.Forms.Label lblGallons;
        private System.Windows.Forms.Label lblMpg;
    }
}

