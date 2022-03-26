#include <stdio.h>
#include <stdlib.h>

// make a dynamic array where each element is a void pointer
struct dynArray {
  void **data;
  int size;
  int capacity;
};

// make a method to initialize a dynArray
void dynArrayInit(struct dynArray *array) 
{
  array->data = malloc(sizeof(void *) * 4);
  array->size = 0;
  array->capacity = 4;
}

// make a method to add an element to the array
void dynArrayAdd(struct dynArray *array, void *element) 
{
  if (array->size == array->capacity) {
    array->capacity *= 2;
    array->data = realloc(array->data, sizeof(void *) * array->capacity);
  }
  array->data[array->size] = element;
  array->size++;
}

// make a method to remove an element from the array
void dynArrayRemove(struct dynArray *array, int index) 
{
  if (index < 0 || index >= array->size) {
    return;
  }
  for (int i = index; i < array->size - 1; i++) {
    array->data[i] = array->data[i + 1];
  }
  array->size--;
}

// make a foreach loop function that can iterate over the array
void dynArrayForeach(struct dynArray *array, void (*func)(void *)) 
{
  for (int i = 0; i < array->size; i++) {
    func(array->data[i]);
  }
}

// make a struct to represent an animal
struct animal {
  char *name;
  int age;
};

// make a method to initialize an animal
void animalInit(struct animal *animal, char *name, int age) 
{
  animal->name = name;
  animal->age = age;
}

// make a method to print an animal
void animalPrint(struct animal *animal) 
{
  printf("%s is %d years old\n", animal->name, animal->age);
}

int main(void) 
{
  // make a few animals
  struct animal cat;
  animalInit(&cat, "cat", 2);
  struct animal dog;
  animalInit(&dog, "dog", 4);

  // make a dynamic array to hold animals
  struct dynArray animals;
  dynArrayInit(&animals);

  // add animals to the array
  dynArrayAdd(&animals, &cat);
  dynArrayAdd(&animals, &dog);

  // print each animal
  dynArrayForeach(&animals, (void (*)(void *)) animalPrint);
}
