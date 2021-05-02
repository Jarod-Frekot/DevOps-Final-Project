Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-18.04"

  config.vm.synced_folder ".", "/felix"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3-venv

    mkdir /app
    cd /app

    python3 -m venv /.venv
    cp /felix/requirements.txt /app
    cp /felix/bot.py /app
    cp /felix/.env /app
    cp /felix/popcat.png /app
    cp -r /felix/moods/ /app
    /.venv/bin/pip install --upgrade pip
    /.venv/bin/pip install -r requirements.txt
    cp /felix/app.service /etc/systemd/system
    systemctl start app
    systemctl enable app
    SHELL
  end
