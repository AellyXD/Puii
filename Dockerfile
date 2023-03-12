FROM aellyxd/puii:main

# set timezone
ENV TZ=Asia/Kolkata



# Railway's banned dependency
RUN if [ ! $RAILWAY_STATIC_URL ]; then pip3 install --no-cache-dir yt-dlp; fi

# changing workdir
COPY . /app/
WORKDIR /app/

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    # cloning the repo and installing requirements.
    && pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install av --no-binary av

# start the bot
CMD ["bash", "startup"]
