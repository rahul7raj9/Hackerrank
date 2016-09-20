// Write your Student class here
class Student{
  public:
    int score[5];
    void input()
        {
        for(int i=0;i<5;i++)
            cin >> score[i];
    }
    int calculateTotalScore()
        {
        int sum=0;
        for(int i=0;i<5;i++)
            sum+=score[i];
        return sum;
    }
    
    
    
};
