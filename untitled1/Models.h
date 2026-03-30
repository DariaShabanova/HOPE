#ifndef MODELS_H
#define MODELS_H

//headers for Client's Model
double CostPerAcquisition (double AcquisitionCost, int UserAcquisition);
double ConversionRate(int UserAcquisition, int Buyers);
std::string CompareCR(int ClientsCR, int ConcurentsCR);

#endif // MODELS_H
