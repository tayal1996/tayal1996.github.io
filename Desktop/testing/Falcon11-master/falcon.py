#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3, os, datetime
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, current_app, flash
from contextlib import closing
from werkzeug.contrib.atom import AtomFeed
from urlparse import urljoin
# Creating the application.
app = Flask(__name__)
app.config.from_object("config")

@app.context_processor
def variables_def():
  return dict(
        websiteName=unicode(app.config["WEBSITENAME"], "utf-8"),
        websiteDesc=unicode(app.config["WEBSITEDESC"], "utf-8"),
        websiteUrl=request.url_root[:-1],
        disqusName=app.config["DISQUSNAME"],
        currentUrl=request.path,
        )

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource(os.path.join(os.getcwd(), "schema.sql"), mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

def get_pages():
  fetch_pages = g.db.execute('select * from pages order by pageid')
  pages = [dict(pageid=y[0], pageurl=y[1], pagetitle=y[2]) for y in fetch_pages.fetchall()]
  return pages

def get_posts():
  posts = ""
  fetch_posts = g.db.execute('select * from posts order by postid desc')
  posts = [dict(postid=x[0], posttitle=x[1], posturl=x[2], postcontent=x[3], postauthor=x[4], postdate=x[5]) for x in fetch_posts.fetchall()]
  return posts

def getPosts(userid):
  posts = ""
  fetch_posts = g.db.execute('select * from posts where postauthor = ? order by postid desc',(userid,))
  posts = [dict(postid=x[0], posttitle=x[1], posturl=x[2], postcontent=x[3], postauthor=x[4], postdate=x[5]) for x in fetch_posts.fetchall()]
  return posts

def single_post(posturl):
  showingpost = g.db.execute('select * from posts where posturl = ?', (posturl,))
  for x in showingpost.fetchall():
    postid, posttitle, posturl, postcontent, postauthor, postdate = x[0], x[1], x[2], x[3], x[4], x[5]
  post = [postid, posttitle, posturl, postcontent, postauthor, postdate]
  return post

def editpost(posturl):
  if session.get('logged_in'):
    getPost = g.db.execute('select * from posts where posturl = ?', (posturl,))
    for n in getPost.fetchall():
      posttitle, posturl, postcontent = n[1], n[2], n[3]
    post = [posttitle, posturl, postcontent]
    return post
  else:
    abort(404)

def single_page(pageurl):
  showingpage = g.db.execute('select * from pages where pageurl= ?', (pageurl,))
  for x in showingpage.fetchall():
    pageid, pageurl, pagetitle, pagecontent, pageauthor, pagedate = x[0], x[1], x[2], x[3], x[4], x[5]
  page = [pageid, pageurl, pagetitle, pagecontent, pageauthor, pagedate]
  return page

def getUserDetail(userid):
  getDetail = g.db.execute('select * from users where userid= ?', (userid,))
  for x in getDetail.fetchall():
    userid, username, password, fullname, emailid, mobile_no = x[0], x[1], x[2], x[3], x[4], x[5]
  profile = [userid, username, password, fullname, emailid, mobile_no]
  return profile

def getPostsWithAuthor(userid):
  getDetail = g.db.execute('select * from posts where postauthor= ? order by postdate',(userid,))
  adminPost = [dict(posturl=detail[2], posttitle=detail[1], postdate=detail[5]) for detail in getDetail.fetchall()]
  print(adminPost)
  return adminPost

def getAdmin(userid):
  getDetail = g.db.execute('select * from users where not userid = ?',(userid,))
  adminProfile = [dict(userid=detail[0], username=detail[1], fullname=detail[3]) for detail in getDetail.fetchall()]
  return adminProfile

def getCommnet(posturl):
  getDetail = g.db.execute('select * from comments where postid = (select postid from posts where posturl= ?)',(posturl,))
  comment = [dict(userid=detail[2], comment=detail[3], cmttime=detail[4]) for detail in getDetail.fetchall()]
  return comment

def editpage(pageurl):
  if session.get('logged_in'):
    getPage = g.db.execute('select * from pages where pageurl = ?', (pageurl,))
    for n in getPage.fetchall():
      pagetitle, pageurl, pagecontent, = n[1], n[2], n[3]
    page = [pageurl, pagetitle, pagecontent]
    return page
  else:
    abort(404)

def getPostid(posturl):
  getDetail = g.db.execute('select postid from posts where posturl= ?',(posturl,))
  for postid in getDetail.fetchall():
    return postid[0]

def checkUsername(username):
  getUser = g.db.execute('select username from users where username= ?',(username,))
  if not getUser.fetchone():
    return True
  return False

def checkUrl(posturl):
  getUrl = g.db.execute('select posturl from posts where posturl= ?',(posturl,))
  if not getUrl.fetchone():
    return True
  return False  

@app.before_request
def before_request():
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
  db = getattr(g, 'db', None)
  if db is not None:
    db.close()

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.route('/')
def show_index():
  return render_template('index.html', posts=get_posts(), pages=get_pages())

@app.route('/post/<posturl>')
def show_post(posturl):
  return render_template('post.html', post=single_post(posturl), comment=getCommnet(posturl),  pages=get_pages())

@app.route('/post/<posturl>/edit')
def postedit(posturl):
  if session.get('logged_in'):
    return render_template('edit.html', post = editpost(posturl), contentType = "post", pages=get_pages())
  else:
    abort(404)

@app.route('/post/<posturl>/delete')
def postdelete(posturl):
  if session.get('logged_in'):
    g.db.execute('delete from posts where posturl = ?', (posturl,))
    g.db.commit()
    return render_template('index.html', posts=get_posts(), pages=get_pages())
  else:
    abort(404)

@app.route('/page/<pageurl>')
def show_page(pageurl):
  return render_template('page.html', page=single_page(pageurl), pages=get_pages())

@app.route('/page/<pageurl>/edit')
def pageedit(pageurl):
  if session.get('logged_in'):
    return render_template('edit.html', post = editpage(pageurl), contentType = "page", pages=get_pages())
  else:
    abort(404)

@app.route('/page/<pageurl>/delete')
def pagedelete(pageurl):
  if session.get('logged_in'):
      g.db.execute('delete from pages where pageurl = ?', (pageurl,))
      g.db.commit()
      return render_template('index.html', posts=get_posts(), pages=get_pages())
  else:
    abort(404)

@app.route('/archive')
def archive():
  if session.get('logged_in'):
    userid = session['userid']
  else:
    return render_template('archive.html', posts=get_posts(), pages=get_pages())

  return render_template('archive.html', posts=getPosts(userid), pages=get_pages())

@app.route('/publish', methods=['GET', 'POST'])
def publish():
  if session.get('logged_in'):
    if request.method == 'POST':
      if not checkUrl(request.form['url']):
        flash('Give different Content Link!')
        return redirect(request.url)
      if request.form["contenttype"] == "post":
        g.db.execute('insert into posts (posttitle, posturl, postcontent, postauthor) values (?, ?, ?, ?)',
                     (request.form['title'], request.form['url'], request.form['content'], session['userid']))
        g.db.commit()
        return redirect(request.url_root)
      else:
        g.db.execute('insert into pages (pagetitle, pageurl, pagecontent, pageauthor) values (?, ?, ?, ?)',
                     (request.form['title'], request.form['url'], request.form['content'], session['userid']))
        g.db.commit()
        return redirect(request.url_root)
    elif request.method == 'GET':
      return render_template('new.html', pages=get_pages())
  else:
    return abort(404)

def make_external(url):
  return urljoin(request.url_root, url)


@app.route('/posts.atom')
def recent_feed():
  feed = AtomFeed('Recent Articles',
                  feed_url=request.url, url=request.url_root)
  articles = get_posts()[:5]
  for y in range(len(articles)):
      feed.add(articles[y]['posttitle'], articles[y]['postcontent'],
               content_type='html',
               url=make_external(articles[y]['posturl']),
               updated=datetime.datetime.strptime(articles[y]['postdate'], '%Y-%m-%d %H:%M:%S'))
  return feed.get_response()

@app.route('/publishedit', methods=['POST'])
def doEdit():
  if session.get('logged_in'):
    if request.method == 'POST':
      if request.form["contenttype"] == "post":
        g.db.execute('UPDATE posts SET posttitle = ?, postcontent = ? WHERE posturl = ?', (request.form['title'], request.form['content'], request.form['url']))
        g.db.commit()
        return redirect(request.url_root)
      else:
        g.db.execute('UPDATE pages SET pagetitle = ?, pagecontent = ? WHERE pageurl = ?', (request.form['title'], request.form['content'], request.form['url']))
        g.db.commit()
        return redirect(request.url_root)
    else:
        abort(404)
  else:
    abort(404)


@app.route('/login', methods=['GET', 'POST'])
def login():
  if session.get('logged_in'):
    return redirect(request.url_root)
  # username = request.form['username'].strip()
  if request.method == 'POST':
    getUser = g.db.execute('select * from users where username = ?', (request.form['username'],))
    userData = getUser.fetchone()
    if not userData:
      flash('Invalid Username!')
      return redirect(request.url)

    userid, username, password, mobile_no  = userData[0], userData[1], userData[2], userData[3]
    userDetail = [userid, username, password, mobile_no] 

    if userDetail[2] != request.form['password']:
      flash('Invalid Password!')
      return redirect(request.url) 
    else:
      session['logged_in'] = True
      session['username'] = request.form['username']
      session['userid'] = userDetail[0]
      return redirect(request.url_root)
  return render_template('login.html', pages=get_pages())

@app.route('/profile')
def getProfile():
  if session.get('userid'):
    userid = session['userid']
  else:
    abort(404)
  if session.get('logged_in'):
    return render_template('profile.html', profile=getUserDetail(userid), pages=get_pages())
  else:
    abort(404)

@app.route('/adminlist')
def getAdminList():
  if session.get('userid'):
    userid = session['userid']
  else:
    abort(404)
  if session.get('logged_in'):
    return render_template('users.html', profile=getAdmin(userid), pages=get_pages())
  else:
    abort(404)

@app.route('/postlist/<userid>')
def getPostList(userid):
  if session.get('logged_in'):
    return render_template('userpost.html', posts=getPostsWithAuthor(userid), pages=get_pages())
  else:
    abort(404)

@app.route('/check-username', methods=['POST'])
def checkUser():
    if checkUsername(request.form['x']):
      return 'Username available!'
    return 'Username already exist!'

@app.route('/check-url', methods=['POST'])
def checkPostUrl():
    if not checkUrl(request.form['x']):
      return 'Give different Content Link!'

@app.route('/register', methods=['GET', 'POST'])
def doRegister():
  if request.method == 'POST':
    if request.form['Register'] == 'User Register':
      if not checkUsername(request.form['username']):
        flash('Username already exist!')
        return redirect(request.url)

  if session.get('logged_in'):
    return redirect(request.url_root)
  if request.method == 'POST':
    if request.form['password'] == request.form['confirmPassword']:
      g.db.execute('insert into users (username, password, fullname, emailid, mobile_no) values (?, ?, ?, ?, ?)',
                   (request.form['username'], request.form['password'], request.form['fullname'], request.form['emailid'], request.form['mobile_no']))
      g.db.commit()
      flash('You have registered successfully!')
      return redirect(request.url)
    else:
      error = 'Invalid password'
      session['error'] = error
      flash('Password do not match!')
      return redirect(request.url) #with message
  return render_template('register.html', pages=get_pages())

@app.route('/submit.comment/<posturl>', methods=['GET', 'POST'])
def doComment(posturl):
  postid = getPostid(posturl)
  if session.get('logged_in'):
    userid = session['userid']
  else:
    userid = 0
  if request.method == 'POST':
    g.db.execute('insert into comments (postid, userid, comment) values (?, ?, ?)',(postid, userid, request.form['comment']))
    g.db.commit()
    return redirect(request.url_root) #error
  else:
    return redirect(request.url_root) #with message

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  return redirect(request.url_root)

if __name__ == "__main__":
  init_db()
  app.run(host='0.0.0.0')
