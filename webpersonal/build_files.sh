python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/
