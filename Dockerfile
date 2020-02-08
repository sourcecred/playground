FROM ruby:2.7.0-alpine3.11
# docker build -t playground .
# docker run -p 4000:4000 playground
# docker run -v $PWD/:/code -p 4000:4000 playground
RUN apk update && apk add git vim build-base
RUN gem install bundler && \
    gem install jekyll
WORKDIR /code
COPY . /code
RUN bundle install
EXPOSE 4000
ENTRYPOINT ["bundle", "exec", "jekyll"]
CMD ["serve", "--host", "0.0.0.0"]
