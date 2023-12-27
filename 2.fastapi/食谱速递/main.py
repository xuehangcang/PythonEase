from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()


# 定义食谱模型
class Recipe(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]


# 存储菜单
fake_db = []


@app.post("/recipes/", response_model=Recipe)
async def create_recipe(recipe: Recipe):
    recipe.id = len(fake_db) + 1
    fake_db.append(recipe)
    return recipe


@app.get("/recipes/", response_model=List[Recipe])
async def get_recipes():
    return fake_db


@app.get("/recipes/{recipe_id}", response_model=Recipe)
async def get_recipe(recipe_id: int):
    recipe = next((rec for rec in fake_db if rec.id == recipe_id), None)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@app.put("/recipes/{recipe_id}", response_model=Recipe)
async def update_recipe(recipe_id: int, recipe: Recipe):
    recipe_index = next((index for (index, rec) in enumerate(fake_db) if rec.id == recipe_id), None)
    if recipe_index is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    fake_db[recipe_index] = recipe
    return recipe


@app.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int):
    global fake_db
    fake_db = [rec for rec in fake_db if rec.id != recipe_id]
    return {"message": "Recipe deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", log_level="info")
