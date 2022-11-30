#include <bits/stdc++.h>
#include <iostream>
#include <time.h>
#include <string.h>
#include <windows.h>

int myPin = 1413;

using namespace std;

double accountBlance = 0;

vector<pair<string, double>> currency;
vector<int> coin;

void setcolorandbackground(int textc, int backg)
{
      WORD color = ((backg & 0x0F) << 4) + (textc & 0x0F);
      SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
}

void title()
{
      system("cls");
      cout << endl;
      setcolorandbackground(9, 0);
      cout << "\t\t\t---------------------------------------------------------" << endl;
      cout << "\t\t\t|";
      setcolorandbackground(14, 0);
      cout << "\tWelcome to The ATM Machin (Team: Alo_Squade)!!";
      setcolorandbackground(9, 0);
      cout << "\t|" << endl;
      cout << "\t\t\t---------------------------------------------------------\n"
           << endl;
}

void firstMenu()
{
      title();
      cout << endl;
      cout << "===================" << endl;
      setcolorandbackground(2, 0);
      cout << "| 1. ATM Machine. |" << endl;
      cout << "| 2. Exit         |" << endl;
      setcolorandbackground(9, 0);
      cout << "===================" << endl;
      setcolorandbackground(21, 0);
      cout << "Enter your Choice: ";
}

void atmMachineOption()
{
      system("cls");
      cout << endl;
      setcolorandbackground(9, 0);
      cout << "=======================" << endl;
      setcolorandbackground(2, 0);
      cout << "| 1. Deposite.        |" << endl;
      cout << "| 2. Check Balance.   |" << endl;
      cout << "| 3. Withdrawal Money.|" << endl;
      cout << "| 4. Convert Currency.|" << endl;
      cout << "| 5. Retail Money.    |" << endl;
      setcolorandbackground(9, 0);
      cout << "=======================" << endl;
      setcolorandbackground(21, 0);
      cout << "Enter your Choice: ";
}

void insectCurrency(string currencyName, double currencyRate)
{
      currency.push_back(make_pair(currencyName, currencyRate));

      for (int i = 0; i < currency.size(); i++)
      {
            for (int j = i + 1; j < currency.size(); j++)
            {
                  if (currency[i].second < currency[j].second)
                  {
                        swap(currency[i].second, currency[j].second);
                        swap(currency[i].first, currency[j].first);
                  }
            }
      }
}

void convertCurrencyf(double currencyConvert, int cSize, double amount)
{
      currencyConvert =
          amount / (currency[(currency.size()) - (cSize)].second);

      cout << endl;
      setcolorandbackground(3, 0);
      cout
          << "Currency rate is: "
          << currency[(currency.size()) - (cSize)].second;

      cout << endl;

      cout
          << "Total ammount is: "
          << fixed
          << setprecision(2)
          << currencyConvert
          << " "
          << currency[(currency.size()) - (cSize)].first;

      cout << endl;
      cout << endl;
      setcolorandbackground(14, 0);
      cout << "Will you withdraw this money?" << endl;
      setcolorandbackground(9, 0);
      cout << "==========" << endl;
      setcolorandbackground(2, 0);
      cout << "| 1. Yes.|" << endl;
      cout << "| 2. No. |" << endl;
      setcolorandbackground(9, 0);
      cout << "==========" << endl;
      setcolorandbackground(21, 0);
      cout << "Chose your option: ";

      int c4;

      cin >> c4;

      if (c4 == 1)
      {
            if (amount > accountBlance)
            {
                  cout << endl;
                  setcolorandbackground(4, 0);
                  cout
                      << "Your account does not have enough balance."
                      << endl;
            }
            else
            {
                  accountBlance -= amount;
                  cout << endl;
                  setcolorandbackground(3, 0);
                  cout
                      << "Withdradal done!"
                      << endl;
            }
      }
}

void coinInsert(double coinItem)
{

      coin.push_back(coinItem);

      for (int i = 0; i < coin.size(); i++)
      {
            for (int j = i + 1; j < coin.size(); j++)
            {
                  if (coin[i] > coin[j])
                  {
                        swap(coin[i], coin[j]);
                  }
            }
      }
}

void minimumNumberOfCoin(int n, int amount)
{
      int solution[n][amount + 1];

      for (int i = 0; i < n; i++)
      {
            solution[i][0] = 0;

            for (int j = 1; j < amount + 1; j++)
            {
                  solution[0][j] = j;
            }
      }

      for (int i = 1; i < n; i++)
      {

            for (int j = 1; j < amount + 1; j++)
            {

                  if (coin[i] > j)
                  {
                        solution[i][j] = solution[i - 1][j];
                  }
                  else
                  {
                        solution[i][j] = min(solution[i - 1][j], 1 + solution[i][j - coin[i]]);
                  }
            }
      }

      cout << endl;
      setcolorandbackground(3, 0);
      cout << "Coin Require: " << solution[n - 1][amount] << endl;
      cout << "Requare coin is: ";

      int i = n - 1;
      int j = amount;
      int mini = solution[i][j];

      while (j != 0)
      {
            if (solution[i - 1][j] == mini)
            {
                  i--;
            }
            else
            {
                  cout << coin[i] << " ";
                  j = j - coin[i];
                  mini = solution[i][j];
            }
      }
      cout << endl;
      cout << endl;
      setcolorandbackground(14, 0);
      setcolorandbackground(14, 0);
      cout << "Will you retail this money?" << endl;
      setcolorandbackground(9, 0);
      cout << "==========" << endl;
      setcolorandbackground(2, 0);
      cout << "| 1. Yes.|" << endl;
      cout << "| 2. No. |" << endl;
      setcolorandbackground(9, 0);
      cout << "==========" << endl;
      setcolorandbackground(21, 0);
      cout << "Chose your option: ";

      int c4;

      cin >> c4;

      if (c4 == 1)
      {
            if (amount > accountBlance)
            {
                  setcolorandbackground(4, 0);
                  cout << endl;
                  cout
                      << "Your account does not have enough balance."
                      << endl;
            }
            else
            {
                  accountBlance -= amount;
                  cout << endl;
                  setcolorandbackground(2, 0);
                  cout
                      << "Withdradal done!"
                      << endl;
            }
      }
}

int main()
{
      int n, e;
      double currencyConvert = 0.0;

      insectCurrency("USD", 101.81);
      insectCurrency("Euro", 106.03);
      insectCurrency("INR", 1.25);
      insectCurrency("Pound", 123.10);

      coinInsert(500.0);
      coinInsert(20.0);
      coinInsert(200.0);
      coinInsert(10.0);
      coinInsert(50.0);
      coinInsert(100.0);
      coinInsert(1.0);
      coinInsert(5.0);
      coinInsert(2.0);

      do
      {
            firstMenu();

            cin >> n;

            switch (n)
            {
            case 1:
                  int pin, adi, sizeFf;
                  do
                  {
                        cout << endl;
                        cout << "Enter your pin: ";
                        cin >> pin;

                        if (pin == myPin)
                        {
                              do
                              {
                                    atmMachineOption();

                                    int m;
                                    cin >> m;
                                    switch (m)
                                    {
                                    case 1:
                                          cout << endl;
                                          setcolorandbackground(14, 0);
                                          cout << "Enter deposite amount: ";
                                          double blance;
                                          cin >> blance;
                                          accountBlance += blance;
                                          break;

                                    case 2:
                                          cout << endl;
                                          setcolorandbackground(14, 0);
                                          cout << "Now your account blance is: "
                                               << accountBlance << " TK" << endl;
                                          break;

                                    case 3:
                                          double moneyWithdrawal;
                                          cout << endl;
                                          setcolorandbackground(14, 0);
                                          cout
                                              << "How many money you withdrawal: ";
                                          cin >> moneyWithdrawal;

                                          if (moneyWithdrawal > accountBlance)
                                          {
                                                cout << endl;
                                                setcolorandbackground(4, 0);
                                                cout
                                                    << "Your account does not have enough balance."
                                                    << endl;
                                          }
                                          else
                                          {
                                                accountBlance -= moneyWithdrawal;
                                                cout << endl;
                                                setcolorandbackground(3, 0);
                                                cout << "Your " << moneyWithdrawal
                                                     << " TK. withdrawal done." << endl;
                                          }

                                          break;

                                    case 4:

                                          cout << endl;
                                          adi = currency.size();
                                          setcolorandbackground(9, 0);
                                          cout << "     _____________" << endl;
                                          cout << "====(Currency List)====" << endl;
                                          cout << "     `````````````" << endl;
                                          setcolorandbackground(2, 0);

                                          for (auto p : currency)
                                          {
                                                cout << (currency.size()) - (--adi)
                                                     << ". "
                                                     << p.first
                                                     << " ---- "
                                                     << p.second
                                                     << endl;
                                          }
                                          setcolorandbackground(9, 0);
                                          cout << "=======================" << endl;
                                          setcolorandbackground(21, 0);
                                          int op;
                                          double amount;

                                          cout << "Chose your option: ";
                                          cin >> op;
                                          setcolorandbackground(14, 0);
                                          cout << "How many money you convert: ";
                                          cin >> amount;

                                          switch (op)
                                          {
                                          case 1:
                                                sizeFf = currency.size();
                                                convertCurrencyf(currencyConvert, sizeFf, amount);
                                                break;

                                          case 2:
                                                sizeFf = currency.size();
                                                convertCurrencyf(currencyConvert, sizeFf - 1, amount);
                                                break;

                                          case 3:
                                                sizeFf = currency.size();
                                                convertCurrencyf(currencyConvert, sizeFf - 2, amount);
                                                break;

                                          case 4:
                                                sizeFf = currency.size();
                                                convertCurrencyf(currencyConvert, sizeFf - 3, amount);
                                                break;

                                          default:
                                                setcolorandbackground(4, 0);
                                                cout << "Wrong option select!"
                                                     << endl;
                                                break;
                                          }

                                          break;

                                    case 5:

                                          cout << endl;
                                          setcolorandbackground(9, 0);
                                          cout << "    _________________" << endl;
                                          cout << "===(Available note is)===" << endl;
                                          cout << "    `````````````````" << endl;
                                          setcolorandbackground(2, 0);

                                          for (int i = 0; i < coin.size(); i++)
                                          {
                                                cout
                                                    << i + 1
                                                    << ". "
                                                    << coin[i]
                                                    << " TK"
                                                    << endl;
                                          }
                                          setcolorandbackground(9, 0);
                                          cout << "=========================" << endl;
                                          setcolorandbackground(14, 0);

                                          int am;
                                          cout << "Enter how many amount to retail: ";
                                          cin >> am;

                                          minimumNumberOfCoin(coin.size(), am);

                                          break;

                                    default:
                                          setcolorandbackground(4, 0);
                                          cout << "Wrong option select!" << endl;
                                          break;
                                    }

                                    cout << endl;
                                    setcolorandbackground(9, 0);
                                    cout << "====================" << endl;
                                    setcolorandbackground(2, 0);
                                    cout << "| 1. ATM Matchine. |" << endl;
                                    cout << "| 2. Main Menu.    |" << endl;
                                    setcolorandbackground(9, 0);
                                    cout << "====================" << endl;
                                    setcolorandbackground(21, 0);
                                    cout << "Chose your option: ";

                                    cin >> e;

                              } while (e == 1);
                        }
                        else
                        {
                              cout << endl;
                              setcolorandbackground(4, 0);
                              cout << "Wrong pin input!"
                                   << endl;
                              setcolorandbackground(21, 0);
                        }

                  } while (pin != myPin);

                  break;
            }

      } while (n != 2);

      return 0;
}