The vending application designed and developed shall do the following:
1. Allow a user to purchase a snack.Upon purchasing a snack, the system will invite the user to enter coins only certain denominations until the amount due is met or exceeded: 
          Upon completing the purchase, the quantity of the snack will be reduced by 1. 
          The machine should sell only one snack per transaction.
          If a snack has a quantity of zero, it shall display * out of stock * and the snack cannotbe purchased.
          The Machine must start with a pool of change totalling £12 
          Change must be dispensed from this pool.
          Any new coins inserted when paying for a snack shall be added to the change pool.
          Note that the machine cannot create change and can only give change from thispool.
          Chain of REsponsibility is used a asuitable design pattern. 
          The Machine shall reject the transaction if the snack is out of stock or the machine is unable to provide change.
                                    
2. A secret admin menu shall be available and accessible from the main menu throughentering a special pin: 1011 and password “A5144l”. 
   The admin menu shall allow foran administrator to: Change the snack prices.
                                                      Increase the change pool.
                                                      See the total amount of money presently in the machine.
