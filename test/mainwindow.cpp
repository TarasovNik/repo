#include <QKeyEvent>
#include <iostream>
#include <string>
#include <cstdlib>
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDoubleValidator>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowTitle("Треугольник ли?");
    ui->groupBox_output->hide();
    ui->lineEdit_1_side->setValidator( new QDoubleValidator(0.00001, 100000, 5, this) );
    ui->lineEdit_2_side->setValidator( new QDoubleValidator(0.00001, 100000, 5, this) );
    ui->lineEdit_3_side->setValidator( new QDoubleValidator(0.00001, 100000, 5, this) );
}


MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_try_again_clicked()
{
    ui->groupBox_output->hide();
    ui->groupBox_input->show();
}

void MainWindow::on_pushButton_varify_triangle_clicked()
{
    double a, b, c;
    ui->groupBox_input->hide();
    a = ui->lineEdit_1_side->text().toDouble();
    b = ui->lineEdit_2_side->text().toDouble();
    c = ui->lineEdit_3_side->text().toDouble();
    if (a == 0 || b == 0 || c == 0) {
        ui->label_massege->setText("Одна из сторон равна 0");
    } else if (a + b > c && a + c > b && b + c > a) {
        if (a*a + b*b == c*c || a*a + c*c ==  b*b || b*b + c*c == a*a) {
            ui->label_massege->setText("Это прямоугольный треугольник");
        }
        else if (a == b && a == c) {
             ui->label_massege->setText("Это равносторонний треугольник");
        }
        else {
             ui->label_massege->setText("Это треугольник");
        }
    } else {
        ui->label_massege->setText("Это не треугольник");
    }
    ui->groupBox_output->show();
}

void MainWindow::on_lineEdit_1_side_editingFinished()
{
}






