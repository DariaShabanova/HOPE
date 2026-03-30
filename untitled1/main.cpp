#include <iostream>
#include "Models.h"
#include <QDebug>

//double CostPerAcquisition (double , int ); //(CPA)-стоимость привлечения одного пользователя.
//{
  //  return AcquisitionCost/UserAcquisition;
//}

//double ConversionRate(int , int ); //(CR) — конверсия. Знакомый любому маркетологу показатель — соотношение количества посетителей сайта и тех, кто купил товар или услугу.
//{
  //return double(Buyers)/UserAcquisition*100;
//}

int main()
{
    //Основные параметры получаемые из бд/сайта
    int UserAcquisition = 1000;  //количество привлечённых пользователей рекламой (UA)
    int Buyers=20; //количество покупателей товара (В)
    double AcquisitionCost=100000;    //(AC) — затраты на привлечение пользователей. маркетинговый бюджет
    qDebug()<<CostPerAcquisition(AcquisitionCost, UserAcquisition);
    //std::cout<<CostPerAcquisition(AcquisitionCost, UserAcquisition);
    qDebug()<<ConversionRate(UserAcquisition, Buyers);

    return 0; //
}
