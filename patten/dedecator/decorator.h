#ifndef _DECORATOR_H_
#define _DECORATOR_H_
class Component{
	public:
		Component(){};
		virtual ~Component(){};

		virtual void operate() = 0;
};

class ConcreteComponentA: public Component{
	public:
		ConcreteComponentA(){};
		~ConcreteComponentA(){};
		void operate();
};
class ConcreteComponentB: public Component{
	public:
		ConcreteComponentB(){};
		~ConcreteComponentB(){};
		void operate();
};

class Decorator{
	public:
		Decorator(){};
		virtual ~Decorator(){};
		void addbehavior();
};
#endif
