FROM theteamultroid/ultroid:main

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN bash installer.sh

# changing workdir
WORKDIR "/root/TeamUltroid"

# start the bot
CMD ["bash", "startup"]
