ARG ALPINE_VERSION
ARG PYTHON_CUSTOM_VERSION

FROM python:${PYTHON_CUSTOM_VERSION}-alpine${ALPINE_VERSION}

WORKDIR /opt/arranger

ARG PYTHON_CUSTOM_VERSION
ENV PYTHON_CUSTOM_VERSION $PYTHON_CUSTOM_VERSION

ARG AWS_CLI_VERSION
ARG IAM_AUTH_VERSION
ARG CDKTF_CLI_VERSION
ARG CDK8S_CLI_VERSION
ARG DYFF_VERSION
ARG HELM_VERSION
ARG INSPEC_VERSION
ARG KUBECTL_VERSION
ARG PYCALL_VERSION
ARG PIPENV_PACKAGE_VERSION
ARG PYTHON_SETUPTOOLS_VERSION

ARG TERRAFORM_VERSION
ARG TFENV_REMOTE
ENV TFENV_REMOTE $TFENV_REMOTE

COPY Pipfile* ./

RUN echo 'gem: --no-document' >> ~/.gemrc
RUN apk add --no-cache \
    bash \
    build-base \
    colordiff \
    curl \
    docker \
    git \
    go \
    jq \
    kubectx \
    libffi-dev \
    librdkafka librdkafka-dev \
    libcap \
    npm \
    openldap-dev \
    openssh \
    openssl openssl-dev \
    python3-dev \
    ruby ruby-bigdecimal ruby-dev ruby-etc ruby-io-console \
    vim \
    yarn \
    yq \
    zlib-dev \
    zsh && \
    go install github.com/homeport/dyff/cmd/dyff@v${DYFF_VERSION} && \
    gem install inspec -v "=${INSPEC_VERSION}" && \
    gem install inspec-bin -v "=${INSPEC_VERSION}" && \
    gem install pycall -v "=${PYCALL_VERSION}" && \
    gem install ed25519 bcrypt_pbkdf && \
    yarn global add cdk8s-cli@$CDK8S_CLI_VERSION && \
    yarn global add cdktf-cli@$CDKTF_CLI_VERSION && \
    yarn global add functions-have-names && \
    yarn cache clean && \
    curl -sLO https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
    mv kubectl /usr/bin/kubectl && \
    chmod +x /usr/bin/kubectl && \
    curl -sL https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v${IAM_AUTH_VERSION}/aws-iam-authenticator_${IAM_AUTH_VERSION}_linux_amd64 --output aws-iam-authenticator && \
    mv aws-iam-authenticator /usr/bin/aws-iam-authenticator && \
    chmod +x /usr/bin/aws-iam-authenticator && \
    git clone https://github.com/tfutils/tfenv.git ~/.tfenv && \
    $HOME/.tfenv/bin/tfenv install $TERRAFORM_VERSION && \
    $HOME/.tfenv/bin/tfenv use $TERRAFORM_VERSION && \
    python -m ensurepip --upgrade && \
    pip install pipenv==${PIPENV_PACKAGE_VERSION} && \
    export PIPENV_VERBOSITY=1 && \
    pipenv --python $PYTHON_CUSTOM_VERSION && \
    pipenv run pip install setuptools==$PYTHON_SETUPTOOLS_VERSION && \
    pipenv sync && \
    pipenv sync --dev && \
    ln -s $(pipenv --venv)/lib/python${PYTHON_CUSTOM_VERSION}/site-packages /opt/site-packages && \
    pipenv run pip cache purge && \
    apk del build-base libffi-dev go openssl-dev python3-dev yarn && \
    rm -f Pipfile* && \
    rm -rf /var/cache/apk/* && \
    rm -fr /tmp/* && \
    rm -fr /root/.cache/pip*

ENTRYPOINT ["/bin/sh", "-c"]
