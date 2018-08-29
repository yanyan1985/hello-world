#include "decorator.h"
#include <iostream>

void ConcreteComponentA::operate(){
	std::cout << "concreteComponet  A::operate" << std::endl;
}
void ConcreteComponentB::operate(){
	std::cout << "concreteComponet B::operate" << std::endl;
}
void Decorator::addbehavior(){
	std::cout << "Decorator addbehavior" << std::endl;
}

int main(){
	ConcreteComponentA p;
	p.operate();
	return 0 ;
}
