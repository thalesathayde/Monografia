require 'digest'
require 'pry'

module Anonimizer
  class Main
    attr_reader :type
  
    FILES_TO_ANONIMIZE_STUDENTS = ['anoSemestreIngresso.pl', 'cidade.pl', 'classeIdadeAluno.pl', 'corAluno.pl',
    'crAluno.pl', 'cursoAluno.pl', 'estadoCivil.pl', 'generoAluno.pl', 'qtdSemTrancados.pl',
    'resultadoAlunoTurma.pl', 'temFacebook.pl', 'temTwitter.pl','evasao.f', 'evasao.n'].freeze
  
    FILES_TO_ANONIMIZE_PROFESSORS = ['classeIdadeProfessor.pl', 'professorTurma.pl'].freeze
  
    FILES_WITH_STUDENT_IDS = ['evasao.f', 'evasao.n'].freeze
    FILE_WITH_PROF_ID = ['classeIdadeProfessor.pl'].freeze
  
      def initialize(type)
        @type = type
      end
      
      def anon!
          files_to_anon = ''  
          if type == :student
            files_to_anon = FILES_TO_ANONIMIZE_STUDENTS
          else
            files_to_anon = FILES_TO_ANONIMIZE_PROFESSORS
          end
            map = random_mapping
            files_to_anon.each do |file|
              begin
              raw_file = File.read(file).split("\n")
              File.open(file + '.anon', 'w') do |f|
                raw_file.each do |line|
                  id = extract_id(line)
                  unless map[id.to_s].nil?
                    new_line = line.gsub(id, map[id.to_s])
                    f.puts new_line
                  end
                end
                f.close
            end
            File.delete(file)
            File.rename(file + '.anon', file)
          rescue => exception
            puts exception
            puts "Something went wrong..."
          end  
        end
        File.delete('idadeAluno.pl') if File.exist?('idadeAluno.pl')
        File.delete('idadeProfessor.pl') if File.exist?('idadeProfessor.pl')
      end

      def random_mapping
        if type == :student
          ids = retrieve_uniq_ids(FILES_WITH_STUDENT_IDS)
          randomize_ids(ids)
        elsif type == :professor
          ids = retrieve_uniq_ids(FILE_WITH_PROF_ID)
          randomize_ids(ids)
        else
          raise Exception, 'This script can only anonimize students or professors.'
        end
      end
    
      def retrieve_uniq_ids(files)
        ids = []
        files.each do |file|
          f = File.open(file, "r")
          f.each_line do |line|
            ids << extract_id(line)
          end
          f.close
        end
        ids
      end
  
    # Example of a line:
    #'curso_aluno(12345679,9)'.split('(')[1].split(',')[0].split(').')[0]"
      def extract_id(line)
        line.split('(')[1].split(',')[0].split(').')[0]
      end
  
      def randomize_ids(ids)
        hash = {}
        ids.each do |id|
          hash["#{id}"] = Random.rand(12345679).to_s + Random.rand(12345679).to_s
        end
        hash
      end
    end
  end

Anonimizer::Main.new(:student).anon!
Anonimizer::Main.new(:professor).anon!