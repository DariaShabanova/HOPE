#include <QCoreApplication>
#include <qdebug.h>
#include <iostream>

//Основные параметры получаемые из бд/сайта
int UserAcquisition; //количество привлечённых пользователей рекламой (UA)
int Buyers; //количество покупателей товара (В)
double AcquisitionCost; //(AC) — затраты на привлечение пользователей. маркетинговый бюджет


//CPA
double CostPerAcquisition (double AcquisitionCost, int UserAcquisition) //(CPA)-стоимость привлечения одного пользователя.
{
  return AcquisitionCost/UserAcquisition;
}

//CR
double ConversionRate(int UserAcquisition, int Buyers) //(CR) — конверсия. Знакомый любому маркетологу показатель — соотношение количества посетителей сайта и тех, кто купил товар или услугу.
{
  return (double) Buyers/UserAcquisition*100;
}

//int ClientsCR = ConversionRate(UserAcquisition, Buyers);//Вычисляемый CR клиента - пользователя
//int ConcurentsCR; //CR конкурентов, получаемый запросом в случае необходимости

std::string CompareCR(int ClientsCR, int ConcurentsCR)
{
    if (ClientsCR < ConcurentsCR)
    {
        return "Sales efficiency is low after customer acquisition. Conversion is below average in the niche.";
    }
    if (ClientsCR > ConcurentsCR)
    {
        return "Conversion rate is higher than the average for the niche";
    }
    if (ClientsCR = ConcurentsCR)
    {
        return "Conversion is normal and corresponds to the average value in the niche";
    }
}

//(CAC)
int TargetologistSalary; //зарплата таргетолога и специолистов по привличнию клиентов.
double AdditionalEngagementServices; //дополнительные расходы на рекламные услуги.

//(CAC)- стоимость привлечения одного клиента.

double CustomerAcquisitionCost(double AcquisitionCost, int TargetologistSalary, double AdditionalEngagementServices, int Buyers) //(CAC)- стоимость привлечения одного клиента.
{
    return ((AcquisitionCost + TargetologistSalary + AdditionalEngagementServices)/Buyers);
}

//(APC)
int SalesAmount;//общее число покупок

double AveragePaymentCount(int SalesAmount, int Buyers) //(APC) — среднее число покупок на одного клиента.
{
    return (double) SalesAmount/Buyers;
}

//AOV-AvP Average Price (AvP) или Average Order Value (AOV) — средний чек.
//Это средняя сумма, которую один клиент тратит за одну покупку или услугу в вашем бизнесе
//за определённый период.
double AllMoney; //вся выручка;

double AveragePrice (int SalesAmount, double AllMoney)
{
    return AllMoney/SalesAmount;
}

//Cost of Goods Sold (COGS) — себестоимость проданных товаров.

double CostofGoodsSold;


