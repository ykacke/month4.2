from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngridientForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('recipe_list')

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
        else:
            form = RecipeForm()
        return render(request, 'recipes/add_recipe.html', {'form': form})

def add_ingredient(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = IngridientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
        else:
            form = IngridientForm()
        return render(request, 'recipes/add_ingredient.html', {'form': form, 'recipe': recipe})