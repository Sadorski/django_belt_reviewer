from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User, UserManager, Book, Review
import bcrypt
  # the index function is called when root is visited
def index(request):
    return render(request, 'beltreviewer/index.html')

def books(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "books": Book.objects.all(),
        "reviews": Review.objects.order_by("-created_at")[0:3]

    }

    return render(request, 'beltreviewer/books.html', context) # /books Template query last 3 ------ > div that shows other books with reviews and alink to the book

def add(request):
    if not 'user_id' in request.session:
        return redirect('/')
    return render(request, 'beltreviewer/add.html')

def review(request, id):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(book_id=id)

    }
    return render(request, 'beltreviewer/bookid.html', context) # /books/<id> all books

def userlist(request, id):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
       'user': User.objects.get(id=id),
       'reviews': Review.objects.filter(user_id=id),
       'count': len(Review.objects.filter(user_id=id))

    }
    return render(request, 'beltreviewer/user.html', context) # /users/id all users

def clear(request):
    request.session.clear()
    return redirect('/')

def process(request):
    if request.method == 'POST':
        if request.POST['action'] == 'register':
            errors = User.objects.basic_validator(request.POST)
            if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')
            else:
                hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'].lower(), password = hash1, username = request.POST['username'])
                user = User.objects.filter(email=request.POST['email'].lower())
                
                request.session['username'] = user[0].username
                request.session['user_id'] = user[0].id
                return redirect ('/books')
        if request.POST['action'] == 'login':
            errors = User.objects.login_validator(request.POST)
            if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect('/')
            user = User.objects.filter(email=request.POST['email'].lower())
            print user
            request.session['username'] = user[0].username
            request.session['user_id'] = user[0].id
            return redirect('/books')
        
        if request.POST['action'] == 'add_book':
            if len(request.POST['author']) > 0:
                author = request.POST['author']
            else:
                author = request.POST['authorlist']
            user = User.objects.get(id=request.session['user_id'])
            Book.objects.create(title=request.POST['title'], author=author)
            book = Book.objects.get(title=request.POST['title'])
            Review.objects.create(desc=request.POST['desc'], rating=request.POST['rating'], user=user, book=book)
            return redirect('/books/{}'.format(book.id))
        
        if request.POST['action'] == 'add_review':
            print "hello"
            user = User.objects.get(id=request.session['user_id'])
            print "1"
            book = Book.objects.get(id=request.POST['bookid'])
            print "2"
            Review.objects.create(desc=request.POST['desc'], rating=request.POST['rating'], user=user, book=book)
            return redirect('/books/{}'.format(request.POST['bookid']))
        
        if request.POST['action'] == 'delete_review':
            a = Review.objects.get(id=request.POST['delreview'])
            id = a.book_id
            print 'hello'
            a.delete()
            print 'goodbye'

            return redirect('/books/{}'.format(id))

            