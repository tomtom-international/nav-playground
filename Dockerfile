ARG PYTHON_BASE=python:3.6.7-alpine3.7
FROM $PYTHON_BASE as builder 

RUN pip install --upgrade virtualenv==16.4.3 && python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY dist /dist
RUN pip install /dist/*

FROM $PYTHON_BASE 
COPY --from=builder /opt/venv /opt/venv

LABEL io.whalebrew.name "nav-playground"
LABEL io.whalebrew.config.working_dir "$PWD"

ENV PATH="/opt/venv/bin:$PATH"
ENTRYPOINT ["nav-playground"]
