from django.shortcuts import render

finches = [
    {
        "name": "Goldie",
        "species": "American Goldfinch",
        "description": "Bright yellow plumage, state bird of New Jersey",
        "age": 7,
    },
    {
        "name": "Rosie",
        "species": "House Finch",
        "description": "Brown plumage, white and brown breast",
        "age": 2,
    },
    {
        "name": "Rocky",
        "species": "Brambling",
        "description": "Orange-breasted, black-headed finch",
        "age": 9,
    },
]


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finches_index(request):
    return render(request, "finches/index.html", {"finches": finches})
