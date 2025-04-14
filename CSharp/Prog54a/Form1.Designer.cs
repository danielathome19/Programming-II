namespace Prog54a {
    partial class Form1 {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            comboBox1 = new ComboBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            lblMiles = new Label();
            lblGallons = new Label();
            lblMpg = new Label();
            button1 = new Button();
            button2 = new Button();
            SuspendLayout();
            // 
            // comboBox1
            // 
            comboBox1.Font = new Font("Segoe UI", 14F, FontStyle.Regular, GraphicsUnit.Point, 0);
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "1970 VW Bug", "1979 Firebird", "1980 Subaru", "1975 Cutlass" });
            comboBox1.Location = new Point(234, 35);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(332, 46);
            comboBox1.TabIndex = 0;
            // 
            // label1
            // 
            label1.BackColor = Color.IndianRed;
            label1.BorderStyle = BorderStyle.FixedSingle;
            label1.Font = new Font("Segoe UI", 14F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label1.ForeColor = Color.White;
            label1.Location = new Point(19, 18);
            label1.Name = "label1";
            label1.Size = new Size(151, 79);
            label1.TabIndex = 1;
            label1.Text = "Car:";
            label1.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label2
            // 
            label2.BackColor = Color.IndianRed;
            label2.BorderStyle = BorderStyle.FixedSingle;
            label2.Font = new Font("Segoe UI", 14F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label2.ForeColor = Color.White;
            label2.Location = new Point(19, 148);
            label2.Name = "label2";
            label2.Size = new Size(151, 58);
            label2.TabIndex = 2;
            label2.Text = "Miles:";
            label2.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label3
            // 
            label3.BackColor = Color.IndianRed;
            label3.BorderStyle = BorderStyle.FixedSingle;
            label3.Font = new Font("Segoe UI", 14F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label3.ForeColor = Color.White;
            label3.Location = new Point(19, 225);
            label3.Name = "label3";
            label3.Size = new Size(151, 58);
            label3.TabIndex = 3;
            label3.Text = "Gallons:";
            label3.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label4
            // 
            label4.BackColor = Color.IndianRed;
            label4.BorderStyle = BorderStyle.FixedSingle;
            label4.Font = new Font("Segoe UI", 14F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label4.ForeColor = Color.White;
            label4.Location = new Point(19, 305);
            label4.Name = "label4";
            label4.Size = new Size(151, 58);
            label4.TabIndex = 4;
            label4.Text = "MPG:";
            label4.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // lblMiles
            // 
            lblMiles.BackColor = Color.LightCoral;
            lblMiles.BorderStyle = BorderStyle.FixedSingle;
            lblMiles.Font = new Font("Segoe UI", 14F, FontStyle.Regular, GraphicsUnit.Point, 0);
            lblMiles.Location = new Point(234, 148);
            lblMiles.Name = "lblMiles";
            lblMiles.Size = new Size(332, 58);
            lblMiles.TabIndex = 5;
            lblMiles.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // lblGallons
            // 
            lblGallons.BackColor = Color.LightCoral;
            lblGallons.BorderStyle = BorderStyle.FixedSingle;
            lblGallons.Font = new Font("Segoe UI", 14F, FontStyle.Regular, GraphicsUnit.Point, 0);
            lblGallons.Location = new Point(234, 225);
            lblGallons.Name = "lblGallons";
            lblGallons.Size = new Size(332, 58);
            lblGallons.TabIndex = 6;
            lblGallons.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // lblMpg
            // 
            lblMpg.BackColor = Color.LightCoral;
            lblMpg.BorderStyle = BorderStyle.FixedSingle;
            lblMpg.Font = new Font("Segoe UI", 14F, FontStyle.Regular, GraphicsUnit.Point, 0);
            lblMpg.Location = new Point(234, 305);
            lblMpg.Name = "lblMpg";
            lblMpg.Size = new Size(332, 58);
            lblMpg.TabIndex = 7;
            lblMpg.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // button1
            // 
            button1.BackColor = Color.Firebrick;
            button1.Font = new Font("Segoe UI", 14F, FontStyle.Bold);
            button1.ForeColor = Color.White;
            button1.Location = new Point(19, 396);
            button1.Name = "button1";
            button1.Size = new Size(260, 92);
            button1.TabIndex = 8;
            button1.Text = "Calculate";
            button1.UseVisualStyleBackColor = false;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.BackColor = Color.Firebrick;
            button2.Font = new Font("Segoe UI", 14F, FontStyle.Bold);
            button2.ForeColor = Color.White;
            button2.Location = new Point(306, 396);
            button2.Name = "button2";
            button2.Size = new Size(260, 92);
            button2.TabIndex = 9;
            button2.Text = "Clear";
            button2.UseVisualStyleBackColor = false;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.DarkRed;
            ClientSize = new Size(585, 506);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(lblMpg);
            Controls.Add(lblGallons);
            Controls.Add(lblMiles);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(comboBox1);
            Name = "Form1";
            Text = "Prog54a";
            ResumeLayout(false);
        }

        #endregion

        private ComboBox comboBox1;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label lblMiles;
        private Label lblGallons;
        private Label lblMpg;
        private Button button1;
        private Button button2;
    }
}
