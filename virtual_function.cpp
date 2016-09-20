class Person
{
    public:
    //static int cur_id;
    char name[100];
    int age ;
    virtual void getdata(){}
    virtual void putdata(){}
    
};
class Professor:public Person
{
    //int Person::cur_id = cur_id+1;
   int getid()
        {
        static int cur_id;
        return ++cur_id;
    }
    public:
    static int cur_id;
    int publications;
    void getdata()
        {
        cin >> name;
        cin >> age;
        cin >> publications;
    }
    void putdata()
        {
        cout << name << ' ';
        cout << age <<  ' ';
        cout << publications << ' ';
        cout <<getid()<<  ' ';
        cout << '\n';
    }
};
class Student:public Person
{
    //int Person::cur_id=cur_id+1;
    int getid()
        {
        static int cur_id;
        return ++cur_id;
    }
    public:
    static int cur_id;
    int marks[6];
    void getdata()
        {
        cin >> name ;
        cin >> age ;
        for (int i=0;i<6;i++)
        cin >> marks[i];
    }
    void putdata()
        {
        cout << name << ' ';
        cout << age <<  ' '; 
        int sum=0;
        for (int i=0;i<6;i++)
            sum+=marks[i];
        cout << sum << ' ';
        cout <<getid()<< ' ';
        cout << '\n';
    }
    
    
    
};
