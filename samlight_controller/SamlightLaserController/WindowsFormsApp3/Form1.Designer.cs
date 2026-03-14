namespace WindowsFormsApp3
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.btn_Init = new System.Windows.Forms.Button();
            this.btnarm = new System.Windows.Forms.Button();
            this.btn_stop = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.txtX = new System.Windows.Forms.TextBox();
            this.txtY = new System.Windows.Forms.TextBox();
            this.lblStatus = new System.Windows.Forms.StatusStrip();
            this.axScSamlightClientCtrl1 = new AxSAMLIGHT_CLIENT_CTRL_OCXLib.AxScSamlightClientCtrl();
            ((System.ComponentModel.ISupportInitialize)(this.axScSamlightClientCtrl1)).BeginInit();
            this.SuspendLayout();
            // 
            // btn_Init
            // 
            this.btn_Init.Font = new System.Drawing.Font("Gulim", 13.875F);
            this.btn_Init.Location = new System.Drawing.Point(102, 269);
            this.btn_Init.Name = "btn_Init";
            this.btn_Init.Size = new System.Drawing.Size(215, 150);
            this.btn_Init.TabIndex = 7;
            this.btn_Init.Text = "Initialize";
            this.btn_Init.UseVisualStyleBackColor = true;
            this.btn_Init.Click += new System.EventHandler(this.btn_Init_Click_1);
            // 
            // btnarm
            // 
            this.btnarm.Font = new System.Drawing.Font("Gulim", 13.875F);
            this.btnarm.Location = new System.Drawing.Point(503, 269);
            this.btnarm.Name = "btnarm";
            this.btnarm.Size = new System.Drawing.Size(204, 150);
            this.btnarm.TabIndex = 6;
            this.btnarm.Text = "ArmLaser";
            this.btnarm.UseVisualStyleBackColor = true;
            this.btnarm.Click += new System.EventHandler(this.btnarm_Click);
            // 
            // btn_stop
            // 
            this.btn_stop.Font = new System.Drawing.Font("Gulim", 13.875F);
            this.btn_stop.Location = new System.Drawing.Point(308, 67);
            this.btn_stop.Name = "btn_stop";
            this.btn_stop.Size = new System.Drawing.Size(214, 157);
            this.btn_stop.TabIndex = 5;
            this.btn_stop.Text = "Stop";
            this.btn_stop.UseVisualStyleBackColor = true;
            this.btn_stop.Click += new System.EventHandler(this.btn_stop_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(228, 496);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(37, 12);
            this.label2.TabIndex = 4;
            this.label2.Text = "X좌표";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(499, 496);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(37, 12);
            this.label3.TabIndex = 3;
            this.label3.Text = "Y좌표";
            // 
            // txtX
            // 
            this.txtX.Location = new System.Drawing.Point(217, 536);
            this.txtX.Name = "txtX";
            this.txtX.Size = new System.Drawing.Size(100, 21);
            this.txtX.TabIndex = 2;
            // 
            // txtY
            // 
            this.txtY.Location = new System.Drawing.Point(503, 536);
            this.txtY.Name = "txtY";
            this.txtY.Size = new System.Drawing.Size(100, 21);
            this.txtY.TabIndex = 1;
            // 
            // lblStatus
            // 
            this.lblStatus.Location = new System.Drawing.Point(0, 658);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(767, 22);
            this.lblStatus.TabIndex = 0;
            // 
            // axScSamlightClientCtrl1
            // 
            this.axScSamlightClientCtrl1.Enabled = true;
            this.axScSamlightClientCtrl1.Location = new System.Drawing.Point(371, 589);
            this.axScSamlightClientCtrl1.Name = "axScSamlightClientCtrl1";
            this.axScSamlightClientCtrl1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axScSamlightClientCtrl1.OcxState")));
            this.axScSamlightClientCtrl1.Size = new System.Drawing.Size(100, 50);
            this.axScSamlightClientCtrl1.TabIndex = 8;
            // 
            // Form1
            // 
            this.ClientSize = new System.Drawing.Size(767, 680);
            this.Controls.Add(this.axScSamlightClientCtrl1);
            this.Controls.Add(this.lblStatus);
            this.Controls.Add(this.txtY);
            this.Controls.Add(this.txtX);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btn_stop);
            this.Controls.Add(this.btnarm);
            this.Controls.Add(this.btn_Init);
            this.Name = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.axScSamlightClientCtrl1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }
        #endregion

        // ✅ 실제 사용하는 컨트롤만 선언
        private System.Windows.Forms.Button btn_Init;
        private System.Windows.Forms.Button btnarm;
        private System.Windows.Forms.Button btn_stop;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtX;
        private System.Windows.Forms.TextBox txtY;
        private System.Windows.Forms.StatusStrip lblStatus;
        private AxSAMLIGHT_CLIENT_CTRL_OCXLib.AxScSamlightClientCtrl axScSamlightClientCtrl1;
    }
}