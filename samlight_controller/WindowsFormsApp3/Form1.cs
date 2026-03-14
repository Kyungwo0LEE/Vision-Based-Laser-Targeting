using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using SAMLIGHT_CLIENT_CTRL_EXLib;
using Newtonsoft.Json.Linq;
using System.Net;
using System.Threading;
using System.Net.Sockets;
using System.Diagnostics;

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
        ScSamlightClientCtrlEx ctrlNew;
        TcpListener server;
        Thread listenThread;
        private bool isLaserArmed = false;
        string targetEntityName = "MarkObject";
        private double lastX = 0, lastY = 0;

        public Form1()
        {
            InitializeComponent();
            listenThread = new Thread(new ThreadStart(StartCommandServer));
            listenThread.IsBackground = true;
            listenThread.Start();
            try
            {
                ctrlNew = new ScSamlightClientCtrlEx();
            }
            catch (Exception ex)
            {
                MessageBox.Show("SAMLight 연결 실패: " + ex.Message);
            }
        }

        private void StartCommandServer()
        {
            server = new TcpListener(IPAddress.Any, 5000);
            server.Start();
            while (true)
            {
                using (TcpClient client = server.AcceptTcpClient())
                using (NetworkStream stream = client.GetStream())
                {
                    byte[] buffer = new byte[1024];
                    int bytesRead = stream.Read(buffer, 0, buffer.Length);
                    if (bytesRead == 0) continue;
                    string jsonData = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                    JObject obj = JObject.Parse(jsonData);
                    double x = (double)obj["x"];
                    double y = (double)obj["y"];
                    this.BeginInvoke(new Action(() =>
                    {
                        ExecuteMarking(x, y);
                    }));
                }
            }
        }

        private void ExecuteMarking(double x, double y)
        {
            if (txtX != null) txtX.Text = x.ToString("F2");
            if (txtY != null) txtY.Text = y.ToString("F2");

            

         //   if (!isLaserArmed)
        //    {
         //       lblStatus.Text = "Status: Laser Not Armed";
          //      return;
          //  }

            if (!isLaserArmed)
            {
                lblStatus.Text = "Status: Laser Not Armed";
                return;
            }


            try
            {
                //ctrlNew.ScExecCommand(21);
                //ctrlNew.ScTranslateEntity(targetEntityName, x - lastX, y - lastY, 0);
                //lastX = x;
                //lastY= y;
                //ctrlNew.ScExecCommand(20);

                //  while (ctrlNew.ScIsMarking() == 1)
                //      Thread.Sleep(10);

                //   ctrlNew.ScMoveAbs(0, 0, 0);
                //   ctrlNew.ScSetScannerPosition(x, y,0);

                //   if (txtX != null) txtX.Text = x.ToString("F2");
                //  if (txtY != null) txtY.Text = y.ToString("F2");
                //lastX = 0;
                //lastY = 0;

                double deltaX = x - lastX;
                double deltaY = y - lastY;

               // ctrlNew.ScExecCommand(21);
                
                ctrlNew.ScTranslateEntity(targetEntityName, deltaX, deltaY, 0);
                lastX = x;
                lastY = y;

                ctrlNew.ScMarkEntityByName(targetEntityName, 0);

                //ctrlNew.ScExecCommand(16);
                

                //    ctrlNew.ScExecCommand(19);
                //   ctrlNew.ScMarkEntityByName(targetEntityName, 0);
                //   ctrlNew.ScExecCommand(16);
                //   ctrlNew.ScExecCommand(21);


            }

            catch (Exception ex)
            {
                Debug.WriteLine(ex.Message);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void btn_Init_Click_1(object sender, EventArgs e)
        {
            try
            {
                ctrlNew.ScExecCommand(20);
                lastX = 0;
                lastY = 0;
             //   isLaserArmed = true;
                lblStatus.Text = "Status: Hardware Initialized";
            }
            catch (Exception ex)
            {
                MessageBox.Show("초기화 실패: " + ex.Message);
                Debug.WriteLine(ex.Message);
            }
        }

        private void btn_stop_Click(object sender, EventArgs e)
        {
            try
            {
                ctrlNew.ScStopMarking();
                isLaserArmed = false;
                lblStatus.Text = "Status: EMERGENCY STOPPED";
                MessageBox.Show("긴급 정지되었습니다. 다시 시작하려면 Initialize부터 수행하세요.");
            }
            catch (Exception ex)
            {
                MessageBox.Show("정지 실패: " + ex.Message);
                Debug.WriteLine(ex.Message);
            }
        }

        private void btnarm_Click(object sender, EventArgs e)
        {
            try
            {
                ctrlNew.ScSetDoubleValue(1, 100);
                ctrlNew.ScExecCommand(19);

                ctrlNew.ScTranslateEntity(targetEntityName, -lastX, -lastY, 0);

                lastX = 0;
                lastY = 0;
                isLaserArmed = true;
                lblStatus.Text = "Status: Laser Armed & Ready";
            }
            catch (Exception ex)
            {
                MessageBox.Show("Arm 실패: " + ex.Message);
                Debug.WriteLine(ex.Message);
            }
        }

        private void toolStripStatusLabel1_Click(object sender, EventArgs e)
        {
        }
    }
}